from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def navigate_to(self,url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_to_load(self,url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_url_contains(self,text):
        self.wait.until(EC.url_contains(text))
