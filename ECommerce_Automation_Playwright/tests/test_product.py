import pytest
from playwright.sync_api import expect

@pytest.mark.skip(reason = "Test case successfully passed")
@pytest.mark.smoke
@pytest.mark.regression
def test_verify_cart_icon_visible_and_enabled(product_page):
    expect(product_page.shopping_cart).to_be_visible()
    expect(product_page.shopping_cart).to_be_enabled()
    product_page.shopping_cart.click()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/cart.html")


def test_select_random_products(product_page):
    total_list = product_page.get_all_product_list()
    selected_products = product_page.select_random_products(total_list)
    assert len(selected_products) == 4 # We choose 4 products randomly
    assert int(product_page.get_cart_item_count()) == len(selected_products) #verify successfuly added to cart

