import pytest
from playwright.sync_api import expect
from utils.logger import logger

#@pytest.mark.skip(reason = "Test case successfully passed")
@pytest.mark.smoke
@pytest.mark.regression
def test_verify_cart_icon_visible_and_enabled(product_page):
    expect(product_page.shopping_cart).to_be_visible()
    expect(product_page.shopping_cart).to_be_enabled()
    product_page.shopping_cart.click()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/cart.html")

@pytest.mark.smoke
@pytest.mark.regression
def test_select_random_products(product_page):
    total_list = product_page.get_all_product_list()
    selected_products = product_page.select_random_products(total_list)
    product_page.add_selected_products_to_cart(selected_products)
    assert len(selected_products) == 4 # We choose 4 products randomly
    assert int(product_page.get_cart_item_count()) == len(selected_products) #verify products successfuly added to cart

@pytest.mark.smoke
@pytest.mark.regression
def test_validate_selected_random_products(product_page,cart_page):
    total_list = product_page.get_all_product_list()
    selected_products = product_page.select_random_products(total_list)
    product_page.add_selected_products_to_cart(selected_products)
    assert len(selected_products) == 4  # We choose 4 products randomly
    product_page.shopping_cart.click()
    assert int(cart_page.get_cart_item_count()) == len(selected_products)
    cart_page_product_list = cart_page.get_cart_page_product_list()
    #asserting selected product list count matches with cart page product list
    print(f"Cart Page Product List:{cart_page_product_list}")
    assert len(cart_page_product_list) == len(selected_products)

@pytest.mark.sorting
@pytest.mark.parametrize("sorting_options",["name-sort-asc","name-sort-desc","price-low-high","price-high-low"],
                         ids=["Sorting-Name Asc","Sorting-Name Desc","Sorting-Price low-high","Sorting-Price high-low"])
def test_sorting_functionality(product_page,sorting_options):
    total_list = product_page.get_all_product_list()

    product_page.select_sorting_option(sorting_options)
    #Getting the product list after sorting

    after_sort_product_list = product_page.get_all_product_list()
    print(f"After Sorting:{after_sort_product_list}")

    #verifying the sorted list is according to name
    is_sorted_right = product_page.verify_product_sorting(total_list,after_sort_product_list,sorting_options)
    assert is_sorted_right ,f"Sorting failed for option: {sorting_options}"

@pytest.mark.resetapp
def test_reset_app_functionality(product_page,cart_page):
    logger.info("Reset App Test functionality Starts")
    total_list = product_page.get_all_product_list()
    selected_products = product_page.select_random_products(total_list)
    product_page.add_selected_products_to_cart(selected_products)
    assert len(selected_products) == 4  # We choose 4 products randomly
    assert int(product_page.get_cart_item_count()) == len(
        selected_products)  # verify products successfuly added to cart

    #Open the menu and click reset app link
    # open menu and click logout
    product_page.open_menu()
    product_page.click_reset_app_link()
    product_page.page.reload()

    #verify cart icon badge
    expect(product_page.shopping_cart_badge).not_to_be_attached()

    #go to cart page
    product_page.shopping_cart.click()

    #Verify theres no product listed
    expect(cart_page.cart_product_container).to_have_count(0)
    logger.info("Reset App Test functionality Finished")








