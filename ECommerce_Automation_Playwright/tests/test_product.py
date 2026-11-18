import pytest
from pages.product_page import ProductsPage
from playwright.sync_api import expect


def test_verify_cart_icon_visible_and_enabled(product_page):
    expect(product_page.shopping_cart).to_be_visible()
    expect(product_page.shopping_cart).to_be_enabled()
    product_page.shopping_cart.click()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/cart.html")
    #cart_item_count =product_page.get_cart_item_count()
    #print(cart_item_count)

def select_random_products(product_page):
    pass

