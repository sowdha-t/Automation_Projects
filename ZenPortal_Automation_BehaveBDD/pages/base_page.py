from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException


class BasePage:
   def __init__(self,driver,timeout=10):
       self.driver = driver
       self.timeout = timeout
       self.wait = WebDriverWait(self.driver, self.timeout)

   def navigate_to_url(self, url):
        self.driver.get(url)

   def wait_for_element_visible(self,locator):
       try:
            return self.wait.until(EC.visibility_of_element_located(locator))
       except TimeoutException:
           raise TimeoutException(f"Element with locator:{locator} was not visible")

   def wait_for_element_invisible(self,locator):
       try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
       except TimeoutException:
           raise TimeoutException(f"Element with locator:{locator} is visible")

   def wait_for_element_clickable(self,locator):
       try:
           return self.wait.until(EC.element_to_be_clickable(locator))
       except TimeoutException:
           raise TimeoutException(f"Element with locator:{locator} was not visible")

   def click_element(self,locator):
       try:
           element = self.wait_for_element_clickable(locator)
           element.click()
       except ElementClickInterceptedException:
           raise ElementClickInterceptedException(f"Another Element blocking the click on locator:{locator}")

   def enter_text(self,locator,text):
       try:
           element = self.wait_for_element_visible(locator)
           element.clear()
           element.send_keys(text)
       except Exception as e:
           raise RuntimeError(f"Failed to Input the text into the locator:{locator}")


   def is_element_visible(self,locator):
       try:
           self.wait.until(EC.visibility_of_element_located(locator))
           return True
       except (TimeoutException,NoSuchElementException):
           return False

   def wait_for_url_contains(self, text):
       self.wait.until(EC.url_contains(text))


