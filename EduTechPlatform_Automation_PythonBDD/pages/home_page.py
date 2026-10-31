from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def load_home_page(self,url):
        self.navigate_to(url)

    def get_home_page_title(self):
        return self.get_page_title()

    def get_home_page_url(self):
        return self.get_current_url()

