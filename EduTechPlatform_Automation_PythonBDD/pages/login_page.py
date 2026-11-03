from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    #Locators
    __email_field = (By.CSS_SELECTOR,"input[id='email']")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "login-btn")

    __email_error_field = (By.CSS_SELECTOR, "#emailgroup .invalid-feedback")
    __password_error_field = (By.CSS_SELECTOR, "div[id='passwordGroup'] div[class='invalid-feedback']")
    __error_fields = {
        "email_field" :__email_error_field,
        "password_field" : __password_error_field
    }

    __input_fields = {
        "email" : __email_field,
        "password" : __password_field
    }


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

    def get_error_message(self, field_name):
        locator = self.__error_fields[field_name]
        element = self.find_visible(locator)
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()

    def is_field_invalid(self, field_name):
        """True if the input box carries Bootstrap's 'is-invalid' class (the red box)."""
        field = self.wait.until(
            EC.presence_of_element_located(self.__email_field)
        )
        self.wait.until(lambda d: "is-invalid" in field.get_attribute("class"))
        return True
