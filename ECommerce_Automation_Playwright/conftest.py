# conftest.py
import pytest
from playwright.sync_api import Page, Playwright

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from config.settings import VALID_USERNAME, VALID_PASSWORD

# We will use the browser, context and page fixtures
# provided by pytest-playwright.

# No custom browser initialization or timeout configuration
# is required at this stage

#Setting the data-test-id to select attributes data-test as configured in SauceDemo App
@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def product_page(logged_in_user):
    return ProductsPage(logged_in_user.page)

@pytest.fixture
def logged_in_user(login_page):
    login_page.navigate("/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return login_page

@pytest.fixture
def cart_page(logged_in_user):
    return CartPage(logged_in_user.page)