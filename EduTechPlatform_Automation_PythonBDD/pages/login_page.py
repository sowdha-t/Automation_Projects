from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    #Locators
    __email_field = (By.CSS_SELECTOR,"input[id='email']")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "login-btn")

    __email_error_field = (By.CSS_SELECTOR, "div[id='emailgroup'] div[class='invalid-feedback']")
    __password_error_field = (By.CSS_SELECTOR, "div[id='passwordGroup'] div[class='invalid-feedback']")
    #__profile_image = (By.XPATH,"(//button[@data-target='#account-box'])[1]")
    #__profile_email_id = (By.XPATH, "(//div[@data-parent='#accountGroup']//small[@class='email-wrap'])[1]")

    __profile_image = (By.XPATH,"(//img[@alt='Profile'])[1]")
    __profile_email_id = (By.CSS_SELECTOR, "#account-boxheader p.break-all")
    __profile_sign_out = (By.XPATH, "(//p[normalize-space()='Sign Out'])[1]")


    def navigate_to_login_page(self,login_url):
        self.navigate_to(login_url)

    def enter_login_details(self,email_text,pswd_text):
        self.type_text(self.__email_field,email_text)
        self.type_text(self.__password_field,pswd_text)

    def submit_login_details(self):
        self.click_element(self.__submit_button)

    def wait_for_profile_image(self):
        self.click_element(self.__profile_image)

    def get_profile_email_details(self):
        self.wait_for_profile_image()
        email_from_profile = self.get_text(self.__profile_email_id)
        return email_from_profile

    def get_email_validation_error_msg(self):
        return self.get_text(self.__email_error_field)

    def get_password_validation_error_msg(self):
        return self.get_text(self.__password_error_field)
