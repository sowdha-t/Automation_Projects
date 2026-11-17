class ProductsPage:
    def __init__(self, page):
        self.page = page
        #Locators
        self._menubar_button= page.locator("#react-burger-menu-btn")
        self._logout_menu_link = page.locator("#logout_sidebar_link")

    def open_menu(self):
        self._menubar_button.click()

    def click_logout(self):
        self._logout_menu_link.click()