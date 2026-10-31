from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    #--------------Navigation--------------
    def navigate_to(self,url):
        self.driver.get(url)

    #------------Page title and current url-------------
    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    #-------------Finding element-----------------
    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    #-----------------Basic Click and Type Operations------------------

    def type_text(self,locator,text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self,locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self,locator):
        element = self.find_element(locator)
        return element.text.strip()

    #----------------URL Related operations

    def wait_for_url_to_load(self,url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_url_contains(self,text):
        self.wait.until(EC.url_contains(text))


