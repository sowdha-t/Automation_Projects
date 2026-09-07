from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    #Encapsulated Private Locators specific to EventHub Login page

    __email_field = (By.ID,"email")
    __password_field = (By.ID,"password")
    __signin_button = (By.ID,"login-btn")

    #Field-level Validation messages
    __email_validation_message = (By.XPATH, "//input[@id='email']/following-sibling::p")
    __password_validation_message = (By.XPATH, "//input[@id='password']/following-sibling::p")

    #Authentication Level Error messages
    __authentication_error = (By.XPATH,"//div[@aria-live='polite']")

    def login_to_eventhub(self,email,password):
        self.type_text(self.__email_field,email)
        self.type_text(self.__password_field,password)
        self.click_element(self.__signin_button)

    def get_email_validation_msg(self):
        return self.get_text(self.__email_validation_message)

    def get_password_validation_msg(self):
        return self.get_text(self.__password_validation_message)

    def get_authentication_error_msg(self):
        return self.get_text(self.__authentication_error)