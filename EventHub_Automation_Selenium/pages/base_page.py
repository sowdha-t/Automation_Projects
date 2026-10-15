from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        config = ConfigReader.get_config()
        self.timeout = config["timeout"]
        self.wait = WebDriverWait(driver,self.timeout)


    #-----------------Navigation--------------
    def navigate(self,url):
        self.driver.get(url)


    #-------------Finding-----------------

    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def check_invisibility_of_elements(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_list_of_elements(self,locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )

    #--------------actions--------------------

    def click_element(self,locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self,locator,text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_visible(locator).text.strip()

    #------------------dropdown selections---------------

    def select_by_value(self,locator,value):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        Select(element).select_by_value(value)

    def get_dropdown_options(self,locator):
        element = self.find_element(locator)
        return [option.get_attribute("value").strip() for option in Select(element).options if option.text.strip()]

    def get_dropdown_value(self,locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return Select(element).first_selected_option.get_attribute("value")


    #-------------------Stale Checks---------------------------------
    def wait_for_stale(self,element):
        return self.wait.until(
            EC.staleness_of(element)
        )

    def is_element_present(self,locator):
        return len(self.driver.find_elements(*locator)) > 0


    def is_visible(self,locator,timeout=2):
        try:
            WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_any_condition(self,*conditions):
        return self.wait.until(EC.any_of(*conditions))

    def wait_for_condition(self,*conditions):
        return self.wait.until(EC.all_of(*conditions))

    #------------------URL Checks

    def wait_for_url_contains(self, url_text):
        self.wait.until(EC.url_contains(url_text))

    #-----------------Sync check - custom made

    def wait_for_text_in_element(self,locator,expected_text):
        self.wait.until(
            lambda driver :
            any (
                expected_text.lower() in element.text.lower()
                for element in driver.find_elements(*locator)
            )
        )

    def wait_for_event_count_to_change(self, locator, old_event_count):
        self.wait.until(
            lambda driver:
            len(driver.find_elements(*locator)) != old_event_count
        )








    
