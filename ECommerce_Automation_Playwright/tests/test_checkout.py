from playwright.sync_api import expect
import pytest

@pytest.mark.checkout
@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_end_to_end(product_page,cart_page,checkout_page):
    #user already logged in and selecting some random products
    total_list = product_page.get_all_product_list()
    selected_products = product_page.select_random_products(total_list)
    product_page.add_selected_products_to_cart(selected_products)
    product_page.shopping_cart.click()
    cart_page_product_list = cart_page.get_cart_page_product_list()
    # asserting selected product list count matches with cart page product list
    print(f"Cart Page Product List:{cart_page_product_list}")
    assert len(cart_page_product_list) == len(selected_products)

    # Validating the product name and product price matches in Cart page

    selected_product_details = {
        (product["product_name"], product["product_price"]) for product in selected_products
    }
    print(f"Selected Products Details:{selected_product_details}")
    cart_product_details = {
        (product["product_name"], product["product_price"]) for product in cart_page_product_list
    }
    print(f"Cart Product Details:{cart_product_details}")

    assert selected_product_details == cart_product_details

    #Moving to Checkout form page
    cart_page.click_checkout_button()

    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    first_name = "TesterFN"
    last_name = "TesterLN"
    zipcode = "123456"
    checkout_page.fill_checkout_form(first_name,last_name ,zipcode)
    checkout_page.click_continue()

    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    #Checkout overview page
    #verifying cart page products correctly listed in checkout overview page
    checkout_page_product_list = checkout_page.get_checkout_page_product_list()

    print(f"Checkout Page Product List:{checkout_page_product_list}")
    assert len(cart_page_product_list) == len(checkout_page_product_list)

    #verifying checkout page product details matches with cart page product list
    # Validating the product name and product price matches in Cart page

    check_out_page_product_details = {
        (product["product_name"], product["product_price"]) for product in checkout_page_product_list
    }
    print(f"Checkout Page Products Details:{check_out_page_product_details}")
    cart_product_details = {
        (product["product_name"], product["product_price"]) for product in cart_page_product_list
    }
    print(f"Cart Product Details:{cart_product_details}")

    assert check_out_page_product_details == cart_product_details

    #Checking the subtotal and total amount of the order

    assert checkout_page.calculate_total_payment(checkout_page_product_list), ("Calculation is not right")

    checkout_page.take_order_screenshot()

    checkout_page.click_finish_order()

    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    expect(checkout_page.get_header_status).to_have_text("Thank you for your order!")










