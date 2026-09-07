from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    #Encapsulated Private Locators specific to EventHub Login page

    __email_field = (By.ID,"email")
    __password_field = (By.ID,"password")
    __signin_button = (By.ID,"login-btn")
    __error_alert = (By.XPATH,"//div[@aria-live='polite']")

    def login_to_eventhub(self,email,password):
        self.type_text(self.__email_field,email)
        self.type_text(self.__password_field,password)
        self.click_element(self.__signin_button)

    def get_error_message(self):
        return self.get_text(self.__error_alert)