from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    #Locators needed for the Dashboard page
    __user_email = (By.ID, "user-email-display")

    def get_user_email(self):
        return self.get_text(self.__user_email)
