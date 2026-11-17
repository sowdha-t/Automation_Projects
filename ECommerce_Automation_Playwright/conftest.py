# conftest.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# We will use the browser, context and page fixtures
# provided by pytest-playwright.

# No custom browser initialization or timeout configuration
# is required at this stage

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def product_page(page: Page):
    return ProductsPage(page)
