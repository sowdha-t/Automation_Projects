class ProductsPage:
    def __init__(self, page):
        self.page = page
        #Locators
        self._menubar_button= page.locator("#react-burger-menu-btn")
        self._logout_menu_link = page.locator("#logout_sidebar_link")

        #cart locators
        self._shopping_cart_icon = page.locator("a[data-test='shopping-cart-link']")
        self._shopping_cart_item_count = page.locator(".shopping_cart_badge")

        #Inventory list items
        self._all_product_list = page.locator(".inventory_item")

    def open_menu(self):
        self._menubar_button.click()

    def click_logout(self):
        self._logout_menu_link.click()

    def get_cart_item_count(self):
        cart_item_count = self._shopping_cart_item_count.inner_text()
        return cart_item_count

    @property
    def shopping_cart(self):
        return self._shopping_cart_icon
