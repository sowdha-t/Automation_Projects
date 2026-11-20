class CartPage:
    def __init__(self,page):
        self.page = page

        #Locators in Cart Page

        #Product details locators
        self._all_product_list = page.get_by_test_id("inventory-item")
        self._checkout_button = page.get_by_test_id("checkout")
        self._continue_shopping_button = page.get_by_test_id("continue-shopping")

        # cart locators
        self._shopping_cart_icon = page.locator("a[data-test='shopping-cart-link']")
        self._shopping_cart_item_count = page.locator(".shopping_cart_badge")

    def get_cart_item_count(self):
        cart_item_count = self._shopping_cart_item_count.inner_text()
        return cart_item_count

    @property
    def shopping_cart(self):
        return self._shopping_cart_icon

    @property
    def cart_product_container(self):
        return self._all_product_list

    def get_cart_page_product_list(self):
        cart_page_product_elements = self._all_product_list
        cart_page_product_elements.first.wait_for()
        cart_page_product_count = cart_page_product_elements.count()
        print(f"cart page product count:{cart_page_product_count}")
        cart_page_product_details = []
        for product_item in cart_page_product_elements.all():
            product_name = product_item.get_by_test_id("inventory-item-name").inner_text().strip()
            product_price = product_item.get_by_test_id("inventory-item-price").inner_text().strip()
            product_quantity = product_item.get_by_test_id("item-quantity").inner_text().strip()
            cart_page_product_details.append({"product_name":product_name,"product_price":product_price,"product_quantity":product_quantity})

        return cart_page_product_details

    def click_checkout_button(self):
        self._checkout_button.click()

