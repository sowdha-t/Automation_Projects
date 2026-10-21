from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ManageEventsPage(BasePage):

    #Getting event details from the All Events Table

    __event_rows = (By.CSS_SELECTOR, "tr[data-testid='event-table-row']")

    __event_titles = (By.CSS_SELECTOR,"tr[data-testid='event-table-row'] td:first-child > span:first-child")

    __event_categories = (By.CSS_SELECTOR,"")

    __event_city = (By.CSS_SELECTOR, "")

    __event_price = (By.CSS_SELECTOR,"")

    __event_seats = (By.CSS_SELECTOR,"")

    #Delete event Locators
    __delete_event_dialog_button = (By.CSS_SELECTOR, "#confirm-dialog-yes")
    __delete_event_dialog_cancel = (By.XPATH,"//button[normalize-space()='Cancel']")
    __delete_event_close_dialog = (By.XPATH,"//button[@aria-label='Close']")

    #Notification Toast message locator
    __notification_message = (
        By.CSS_SELECTOR,
        "div[aria-live='polite'] p"
    )

    def get_notification_message(self):
        return self.get_text(self.__notification_message)


    def get_all_event_titles(self):
        elements = self.get_list_of_elements(self.__event_titles)
        titles = [element.text.strip() for element in elements]
        print(f"Event Title Names:{titles}")
        print(f"No. of Events:{len(titles)}")
        return titles

    def is_event_displayed_in_table(self,event_title):
        event_titles = self.get_all_event_titles()
        return event_title in event_titles

    def get_event_row(self,event_title):
        rows = self.get_list_of_elements(self.__event_rows)

        for row in rows:
            title = row.find_element(By.CSS_SELECTOR,"td:first-child span:first-child").text.strip()
            if title == event_title:
                return row

        raise AssertionError(
            f"Event {event_title} was not found in the Event Table"
        )

    def get_event_details(self,event_title):
        self.scroll_to_view_element(self.__event_rows)
        rows = self.get_list_of_elements(self.__event_rows)
        print(f"Length of rows:{len(rows)}")
        event_details = {}
        for row in rows:
            title = row.find_element(By.CSS_SELECTOR, "td:first-child span:first-child").text.strip()
            print(title)
            if title == event_title:
                event_category = row.find_element(By.CSS_SELECTOR,"td:nth-child(2)").text.strip()
                event_city = row.find_element(By.CSS_SELECTOR,"td:nth-child(3)").text.strip()
                event_date = row.find_element(By.CSS_SELECTOR,"td:nth-child(4)").text.strip()
                event_price = row.find_element(By.CSS_SELECTOR,"td:nth-child(5").text.strip().removeprefix("$")
                print(event_price)
                event_total_seats = row.find_element(By.CSS_SELECTOR,"td:nth-child(6)").text.strip()
                event_details["event_title"] = title
                event_details["event_category"] =event_category
                event_details["event_city"] =event_city
                event_details["event_date"] =event_date
                event_details["event_price"] =event_price
                event_details["event_total_seats"] =event_total_seats

                return event_details

            else:
                continue

        raise AssertionError(
            f"Event {event_title} was not found in the Event Table"
        )


    def click_edit_event(self,event_title):
        row = self.get_event_row(event_title)

        self.scroll_to_view_element(self.__event_rows)

        edit_button = row.find_element(By.CSS_SELECTOR,"[data-testid='edit-event-btn']")

        self.click_element(edit_button)



    def click_delete_event(self,event_title):

        row = self.get_event_row(event_title)

        self.scroll_to_view_element(self.__event_rows)

        delete_button = row.find_element(By.CSS_SELECTOR,"[data-testid='delete-event-btn']")

        self.click_element(delete_button)

        #Deleting the button in Dialog box
        self.click_element(self.__delete_event_dialog_button)

        message = self.get_notification_message()


    def cancel_delete_event(self,event_title,cancel_check):
        row = self.get_event_row(event_title)

        self.scroll_to_view_element(self.__event_rows)
        delete_button = row.find_element(By.CSS_SELECTOR, "[data-testid='delete-event-btn']")
        self.click_element(delete_button)

        if cancel_check == "cancel_check": # user clicks the cancel button in the dialog box
            self.click_element(self.__delete_event_dialog_cancel)
        # Cancelling the button in Dialog box
        elif cancel_check == "close_check": #user closes the dialog box
            self.click_element(self.__delete_event_close_dialog)




