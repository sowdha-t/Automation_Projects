from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

class AddEventPage(BasePage):

    #------------Locators------------
    __event_title = (By.CSS_SELECTOR,"#event-title-input")
    __event_description = (By.CSS_SELECTOR,"textarea[placeholder*='event']")
    __event_category = (By.ID,"category")
    __event_city = (By.ID,"city")
    __event_venue = (By.ID, "venue")
    __event_date_time = (By.ID,"event-date-&-time")
    __event_price = (By.ID,"price-($)")
    __event_total_seats = (By.ID, "total-seats")
    __event_image_url_link = (By.ID,"image-url-(optional)")
    __add_event_button = (By.ID,"add-event-btn") # This is same for update event button too
    __loading_spinner = (
        By.CSS_SELECTOR,
        "#add-event-btn svg.animate-spin"
    )
    __notification_message = (
        By.CSS_SELECTOR,
        "div[aria-live='polite'] p"
    )

    __cancel_edit_button = (
        By.XPATH,
        "//button[normalize-space()='Cancel edit']"
    )
    def wait_for_spinner_to_disappear(self):
        self.wait_for_element_to_disappear(self.__loading_spinner)

    def wait_for_spinner_to_appear(self):
        self.wait_for_element_to_appear(self.__loading_spinner)


    def get_notification_message(self):
        return self.get_text(self.__notification_message)

    def create_new_event(self,event_creation_data):
        title = event_creation_data["event_title"]
        description = event_creation_data["event_description"]
        category = event_creation_data["event_category"]
        city = event_creation_data["event_city"]
        venue = event_creation_data["event_venue"]

        price = event_creation_data["event_price"]
        total_seats = event_creation_data["event_total_seats"]
        image_url = event_creation_data["event_image_url"]

        #Taking the event created time and date
        if event_creation_data["event_date"] == None :
            event_date = datetime.now() + timedelta(days=30)
            formatted_date = event_date.strftime("%Y-%m-%dT%H:%M")
        else:
            formatted_date = event_creation_data["event_date"]

        print("Generated event date:", formatted_date)

        #---------------------Entering the data into the form for Event Creation

        self.type_text(self.__event_title,title)
        self.type_text(self.__event_description,description)
        self.select_by_value(self.__event_category,category)
        self.type_text(self.__event_city,city)
        self.type_text(self.__event_venue,venue)
        #self.type_text(self.__event_date_time,formatted_date)

        date_element = self.find_visible(self.__event_date_time)
        date_element.clear()
        self.input_to_readonly_textbox(date_element,formatted_date)
        print("Date after typing:", date_element.get_attribute("value"))

        self.type_text(self.__event_price,price)
        self.type_text(self.__event_total_seats,total_seats)
        self.type_text(self.__event_image_url_link,image_url)
        self.scroll_to_view_element(self.__add_event_button)
        self.click_element(self.__add_event_button)


        notification_msg = self.get_notification_message()
        print("Notification message:", notification_msg)
        return notification_msg


    def update_event(self,update_event_data):
        field_locators = {
            "event_title": self.__event_title,
            "event_description": self.__event_description,
            "event_city": self.__event_city,
            "event_venue": self.__event_venue,
            "event_price": self.__event_price,
            "event_total_seats": self.__event_total_seats,
            "event_image_url": self.__event_image_url_link
        }

        for field, value in update_event_data.items():

            if field == "event_category":
                self.select_by_value(self.__event_category, value)
            elif field == "event_date":
                date_element = self.find_visible(self.__event_date_time)
                self.input_to_readonly_textbox(date_element,value)
            elif field in field_locators:
                self.type_text(field_locators[field], value)
            else:
                print(f"Test Case details Field:{field}")
                continue

        self.scroll_to_view_element(self.__add_event_button)
        self.click_element(self.__add_event_button)
        self.wait_for_element_to_appear(self.__notification_message)
        return self.get_notification_message()


    def cancel_edit_event(self):
        self.click_element(self.__cancel_edit_button)





