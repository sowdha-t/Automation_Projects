from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        config = ConfigReader.get_config()
        self.timeout = config["timeout"]
        self.wait = WebDriverWait(driver,self.timeout)

    def click_element(self,locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self,locator,text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    
