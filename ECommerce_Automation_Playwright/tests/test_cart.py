import pytest

@pytest.mark.cart_validation
@pytest.mark.regression
@pytest.mark.smoke
def test_validate_cart_page_product_list(product_page,cart_page):
    total_list = product_page.get_all_product_list()
    selected_products = product_page.select_random_products(total_list)
    product_page.add_selected_products_to_cart(selected_products)
    product_page.shopping_cart.click()
    cart_page_product_list = cart_page.get_cart_page_product_list()
    # asserting selected product list count matches with cart page product list
    print(f"Cart Page Product List:{cart_page_product_list}")
    assert len(cart_page_product_list) == len(selected_products)

    #Validating the product name and product price matches in Cart page
    matching_product = []
    for selected_product in selected_products:
        product_name = selected_product["product_name"]
        product_price = selected_product["product_price"]
        product_found = False
        for cart_product in cart_page_product_list:
            if cart_product["product_name"] == product_name:
                product_found = True
                assert cart_product["product_price"] == product_price
                assert int(cart_product["product_quantity"]) == 1
        matching_product.append(product_found)
    print(f"Matching Products Found:{matching_product}")
    assert len(matching_product) == len(selected_products)
    assert all(matching_product)

    #Trying second approach
    selected_product_details = {
        (product["product_name"],product["product_price"]) for product in selected_products
    }
    print(f"Selected Products Details:{selected_product_details}")
    cart_product_details = {
        (product["product_name"], product["product_price"]) for product in cart_page_product_list
    }
    print(f"Cart Product Details:{cart_product_details}")

    assert selected_product_details == cart_product_details
    assert len(matching_product) == len(selected_products)


