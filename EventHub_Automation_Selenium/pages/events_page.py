from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from config import config


class EventsPage(BasePage):
    #Locators present in the Events page
    __eventhub_main_dashboard_link = (By.LINK_TEXT, "EventHub")
    __search_events_input_box = (By.XPATH,"//input[contains(@placeholder,'Search')]")
    __all_categories_dropdown = (By.XPATH, "//option[text()='All Categories']/ancestor::select")
    __all_cities_dropdown = (By.XPATH, "//option[text()='All Cities']/ancestor::select")

    #Featured Events section in the Events page
    __all_events_displayed = (By.CSS_SELECTOR, "#event-card")
    __event_names = (By.CSS_SELECTOR, "[data-testid='event-card'] h3")
    __event_categories = (By.XPATH, "//article[@data-testid='event-card']//div[@class='absolute top-3 left-3']/span")
    __event_cities_elements = (By.XPATH,"//article[@data-testid='event-card']//div[contains(@class,'space-y-1.5')]//div[2]/span")
    __book_now_button_list = (By.CSS_SELECTOR,"[data-testid='book-now-btn']")

    #Clear filter button and Add New Event  button at the bottom of the page
    __clear_filter_button = (By.XPATH, "//button[normalize-space()='Clear filters']")
    __add_new_event_button = (By.XPATH, "//button[text()='Add New Event']")

    #No Events found message
    __no_events_found_message = (By.XPATH,"//h3[normalize-space()='No events found']")

    def navigate_to_events_page(self):
        events_url = config.BASE_URL + config.EVENTS_URL
        self.driver.get(events_url)
        self.wait_for_url_contains(config.EVENTS_URL)


    def search_valid_event(self,search_text):
        initial_event_count = self.get_event_count()
        self.type_text(self.__search_events_input_box,search_text)

        self.wait_for_event_count_to_change(
            self.__all_events_displayed,
            initial_event_count)

    def search_invalid_event(self,search_text):
        self.type_text(self.__search_events_input_box, search_text)
        event_list = self.check_invisibility_of_elements(self.__all_events_displayed)
        return event_list


    def get_all_events(self):
        return self.get_list_of_elements(self.__all_events_displayed)

    def get_event_count(self):
        return len(self.get_all_events())

    def get_event_names(self):
        event_names_element = self.get_list_of_elements(self.__event_names)
        return [event.text for event in event_names_element]

    def get_event_locations(self):
        city_locations = self.get_list_of_elements(self.__event_cities_elements)
        return [city.text.strip() for city in city_locations]


    def get_no_events_message(self):
        return self.get_text(self.__no_events_found_message)

    def category_based_search(self,search_text):
        #Getting the initial list of events
        initial_event_list = self.get_all_events()
        #length_initial_event_list = len(initial_event_list)

        #Selecting a search value in the dropdown
        self.select_by_value(self.__all_categories_dropdown,search_text)
        #Waiting for the DOM to rerender

        self.wait_for_stale(initial_event_list[0])

        self.wait_for_any_condition(
            EC.visibility_of_element_located(self.__event_categories),
            EC.visibility_of_element_located(self.__no_events_found_message)
        )


        if self.is_element_present(self.__no_events_found_message):
            print(self.get_text(self.__no_events_found_message))
            print(f"No Events appeared for the selected category:{search_text}")
            return False

        try:
            filtered_event_categories =  self.get_list_of_elements(self.__event_categories)
        except TimeoutException:
            print(self.get_text(self.__no_events_found_message))
            print(f"No Events appeared for the selected category:{search_text}")
            return False

        for event in filtered_event_categories:
            if event.text != search_text:
                break
        else:
            return True

        return False


    def verify_all_dropdown_category_search(self,category_values_to_test):
        actual_result = []
        #Loop through the list of values, handles re-renders and verify the fresh DOM
        dropdown_options = self.get_dropdown_options(self.__all_categories_dropdown)
        print(f"Category values to test:{category_values_to_test}")
        print(f"All dropdown options:{dropdown_options}")

        for category_value in category_values_to_test:
            selected_category_details_dict = {}
            print(f"Testing the dropdown value:{category_value}")

            #check for event list or no records found before proceding with category list to be chosen
            initial_event_list = self.driver.find_elements(
                *self.__all_events_displayed
            )
            self.select_by_value(self.__all_categories_dropdown, category_value)
            selected_category_details_dict["selected_value"] = category_value
            #if initial_event_list:


            self.wait_for_any_condition(
                EC.visibility_of_element_located(self.__all_events_displayed),
                EC.visibility_of_element_located(self.__no_events_found_message)
            ) or self.wait_for_stale(initial_event_list[0])

            no_event_check= self.is_visible(self.__no_events_found_message)

            if no_event_check:
                selected_category_details_dict["result_type"] = "not_found"
                selected_category_details_dict["actual_categories"] = []
                actual_result.append(selected_category_details_dict)
                print(f"This category does not have any events/records:{category_value}")
                continue

            fresh_event_list = self.get_list_of_elements(self.__event_categories)
            fresh_event_category_name = []
            print(f"Found fresh event list:{len(fresh_event_list)}")

            if len(fresh_event_list) > 0:
                selected_category_details_dict["result_type"] = "found"
                for event in fresh_event_list:
                    fresh_event_category_name.append(event.text.strip())

            selected_category_details_dict["actual_categories"] = fresh_event_category_name
            actual_result.append(selected_category_details_dict)

        return actual_result


    def city_based_search(self,search_text):
        #Getting the initial list of events
        initial_event_list = self.get_all_events()
        #length_initial_event_list = len(initial_event_list)

        #Selecting a search value in the dropdown
        self.select_by_value(self.__all_cities_dropdown,search_text)
        #Waiting for the DOM to rerender

        self.wait_for_stale(initial_event_list[0])

        self.wait_for_any_condition(
            EC.visibility_of_element_located(self.__event_categories),
            EC.visibility_of_element_located(self.__no_events_found_message)
        )


        if self.is_element_present(self.__no_events_found_message):
            print(self.get_text(self.__no_events_found_message))
            print(f"No Events appeared for the selected category:{search_text}")
            return False

        try:
            filtered_event_categories =  self.get_event_locations()
        except TimeoutException:
            print(self.get_text(self.__no_events_found_message))
            print(f"No Events appeared for the selected category:{search_text}")
            return False

        for city_location in filtered_event_categories:
            print(f"City Location:{city_location}")
            print(f"Search Text:{search_text}")
            city_name = city_location.split(",")[-1]
            print(f"City Name:{city_name.strip()}")
            if  city_name.strip() != search_text:
                break
        else:
            return True

        return False

    """ These methods is used to verify the functionality of Clear filter button"""


    def is_clear_filters_button_visible(self):
        return self.is_visible(self.__clear_filter_button)

    def clear_filters(self):
        self.click_element(self.__clear_filter_button)

    def get_search_text_box_value(self):
        return self.driver.find_element(*self.__search_events_input_box).get_attribute("value")

    def verify_clear_filter_functionality(self,search_text, category, city):

        results = {}

        #-----------------Search Filter---------------
        self.type_text(self.__search_events_input_box,search_text)

        results["search_filter"] = {
            "button_visible_after_filter" : self.is_clear_filters_button_visible()
        }

        self.clear_filters()

        results["search_filter"].update({
            "button_visible_after_clear" : self.is_clear_filters_button_visible(),
            "search_value_after_clear" : self.get_search_text_box_value()
        })

        #----------------------Category Filter--------------------
        self.select_by_value(self.__all_categories_dropdown,category)

        results["category_filter"] ={
            "button_visible_after_filter" : self.is_clear_filters_button_visible()
        }

        self.clear_filters()

        results["category_filter"].update({
            "button_visible_after_clear": self.is_clear_filters_button_visible(),
            "category_value_after_clear": self.get_dropdown_value(self.__all_categories_dropdown)

        })

        #-----------------------City Filter------------------------
        self.select_by_value(self.__all_cities_dropdown, city)
        results["city_filter"] = {
            "button_visible_after_filter" : self.is_clear_filters_button_visible()
        }

        self.clear_filters()

        results["city_filter"].update({
            "button_visible_after_clear" : self.is_clear_filters_button_visible(),
            "city_value_after_clear" : self.get_dropdown_value(self.__all_cities_dropdown)

        })

        return results



