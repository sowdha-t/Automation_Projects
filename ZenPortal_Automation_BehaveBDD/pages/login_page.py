from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    #Locators from the login page
    __email_field = (By.ID,":r1:")
    __password_field = (By.CSS_SELECTOR,"input[type='password']")
    __submit_button = (By.CSS_SELECTOR,"button[type='submit']")
    __email_error_field = (By.ID,":r1:-helper-text")
    __password_error_field = (By.ID, ":r2:-helper-text")
    __error_fields = {
        "email": __email_error_field,
        "password": __password_error_field
    }

    __modal_popup = (By.XPATH, "//div[@class='mobile-app-promotion-main-div']")
    __modal_popup_close_button = (By.XPATH, "//button[@aria-label='Close popup']")
    __dashboard_header = (By.CSS_SELECTOR,"p.header-name")
    __profile_icon = (By.CSS_SELECTOR,"#profile-click-icon")
    __logout_link = (By.XPATH,"//div[text()='Log out']")


    def login_to_portal(self,email_text,password_text):
        self.enter_text(self.__email_field,email_text)
        self.enter_text(self.__password_field,password_text)

    def submit_login(self):
        self.click_element(self.__submit_button)


    def verify_email_present(self):
        return self.is_element_visible(self.__email_field)

    def verify_password_present(self):
        return self.is_element_visible(self.__password_field)

    def verify_submit_button_present(self):
        return self.is_element_visible(self.__submit_button)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def get_email_validation_message(self):
        return self.wait_for_element_visible(
            self.__email_error_field
        ).text

    def get_password_validation_message(self):
        return self.wait_for_element_visible(
            self.__password_error_field
        ).text

    def get_error_message(self, field_name):
        locator = self.__error_fields[field_name]
        element = self.wait_for_element_visible(locator)
        self.wait.until(lambda d: element.text.strip() != "")
        return element.text.strip()


    def verify_dashboard_header(self):
        dashboard_header = self.wait_for_element_visible(self.__dashboard_header).text
        return dashboard_header

    def logout(self):
        # Check if the modal is visible
        modal = self.wait_for_element_visible(self.__modal_popup)
        print("Modal appeared! Proceeding to interact with it.")
        self.wait_for_element_clickable(self.__modal_popup_close_button).click()
        self.wait_for_element_invisible(self.__modal_popup)
        self.click_element(self.__profile_icon)
        self.click_element(self.__logout_link)


