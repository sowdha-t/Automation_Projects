from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    #Locators
    __login_button = (By.XPATH,"(//button[@id='login-btn' and text()='Login'])[1]")
    __signup_button = (By.XPATH, "(//button[normalize-space()='Sign up'])[1]")

    def __init__(self,driver):
        super().__init__(driver)

    def load_home_page(self,url):
        self.navigate_to(url)

    def get_home_page_title(self):
        return self.get_page_title()

    def get_home_page_url(self):
        return self.get_current_url()

    def check_login_displayed(self):
        return self.find_visible(self.__login_button)

    def click_login_button(self):
        self.click_element(self.__login_button)

    def check_signup_displayed(self):
        return self.find_visible(self.__signup_button)

    def click_signup_button(self):
        self.click_element(self.__signup_button)

