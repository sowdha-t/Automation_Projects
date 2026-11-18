import random
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
        self._all_product_list = page.get_by_test_id("inventory-item")

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

    def get_all_product_list(self):
        all_product_list_elements = self._all_product_list
        all_product_list_elements.first.wait_for()
        product_count = all_product_list_elements.count()
        print(f"product_count:{product_count}")
        all_products_details = []
        for product_item in all_product_list_elements.all():
            product_name = product_item.get_by_test_id("inventory-item-name").inner_text().strip()
            product_item_description = product_item.get_by_test_id("inventory-item-desc").inner_text().strip()
            product_price = product_item.get_by_test_id("inventory-item-price").inner_text().strip()
            all_products_details.append ({"product_name":product_name,"price":product_price})

        return all_products_details

    def select_random_products(self,all_product_list,choice=4):
        #choosing random 4 products
        selected_products = random.sample(all_product_list,choice)
        print(f"selected_products:{selected_products}")
        return selected_products


    def add_selected_products_to_cart(self,selected_products):
        for product in selected_products:
            self.add_product_to_cart(product["product_name"])


    def add_product_to_cart(self,product_name):
        product_item= self._all_product_list.filter(has_text=product_name)
        product_item.get_by_role("button", name='Add to cart').click()





