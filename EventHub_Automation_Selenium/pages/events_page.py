from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class EventsPage(BasePage):
    #Locators present in the Events page
    __eventhub_main_dashboard_link = (By.LINK_TEXT, "EventHub")
    __search_events_input_box = (By.XPATH,"//input[contains(@placeholder,'Search')]")
    __all_categories_dropdown = (By.XPATH, "(//select)[1]")
    __all_cities_dropdown = (By.XPATH, "(//select)[2]")

    #Featured Events section in the Events page
    __all_events_displayed = (By.CSS_SELECTOR, "#event-card")
    __event_names = (By.CSS_SELECTOR, "[data-testid='event-card'] h3")
    __book_now_button_list = (By.CSS_SELECTOR,"[data-testid='book-now-btn']")

    #Add New Event  button at the bottom of the page
    __add_new_event_button = (By.XPATH, "//button[text()='Add New Event']")

    def search_event(self,search_text):
        self.type_text(self.__search_events_input_box,search_text)

    def get_all_events(self):
        return self.get_list_of_elements(self.__all_events_displayed)

    def get_event_count(self):
        return len(self.get_all_events())

    def get_event_names(self):
        event_names_element = self.get_list_of_elements(self.__event_names)
        return [event.text for event in event_names_element]


