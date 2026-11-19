class CheckoutPage:
    def __init__(self, page):
        self.page = page

        #checkout form locators
        self._firstname_field = page.get_by_placeholder("First Name")
        self._lastname_field = page.get_by_placeholder("Last Name")
        self._zipcode_field = page.get_by_test_id("postalCode")
        self._continue_button_field = page.get_by_test_id("continue")
        self._cancel_button_field = page.get_by_role("button", name="Cancel")

        #Checkout page product list locators
        self._checkout_product_list = page.get_by_test_id("inventory-item")

        #Checkout page payment related locators
        self._subtotal_amount_field = page.get_by_test_id("subtotal-label")
        self._tax_amount_field = page.get_by_test_id("tax-label")
        self._payment_total_amount_field = page.get_by_test_id("total-label")

        #Finish and cancel buttons
        self._finish_order_button = page.get_by_role("button", name="Finish")
        self._cancel_checkout_button = page.get_by_role("button", name="Cancel")

        #After submission
        self._order_completion_status = page.get_by_test_id("complete-header")
        self._back_home_button = page.get_by_test_id("back-to-products")
        self._generate_pdf_button = page.get_by_test_id("generate-pdf-order")


    def fill_checkout_form(self,firstname,lastname,zipcode):
        self._firstname_field.fill(firstname)
        self._lastname_field.fill(lastname)
        self._zipcode_field.fill(zipcode)

    def click_continue(self):
        self._continue_button_field.click()

    def click_cancel_in_checkout_form(self):
        self._cancel_button_field.click()

    def click_finish_order(self):
        self._finish_order_button.click()

    def cancel_checkout_in_checkout_final(self):
        self._cancel_checkout_button.click()

    def get_checkout_page_product_list(self):
        checkout_page_product_elements = self._checkout_product_list
        checkout_page_product_elements.first.wait_for()
        checkout_page_product_count = checkout_page_product_elements.count()
        print(f"checkout page product count:{checkout_page_product_count}")
        checkout_page_product_details = []
        for product_item in checkout_page_product_elements.all():
            product_name = product_item.get_by_test_id("inventory-item-name").inner_text().strip()
            product_price = product_item.get_by_test_id("inventory-item-price").inner_text().strip()
            product_quantity = product_item.get_by_test_id("item-quantity").inner_text().strip()
            checkout_page_product_details.append(
                {"product_name": product_name, "product_price": product_price, "product_quantity": product_quantity})

        return checkout_page_product_details


    @property
    def get_header_status(self):
        return self._order_completion_status