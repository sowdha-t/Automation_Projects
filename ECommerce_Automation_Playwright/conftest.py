# conftest.py
import base64
from pathlib import Path
import pytest_html
import pytest
from playwright.sync_api import Page, Playwright

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
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

@pytest.fixture
def checkout_page(logged_in_user):
    return CheckoutPage(logged_in_user.page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_dir = Path("reports/screenshots")
            screenshot_dir.mkdir(parents=True,exist_ok=True)

            screenshot_path = screenshot_dir / f"{item.name}.png"
            page.screenshot(path = str(screenshot_path))
            print(f"failure screenshot saved to {screenshot_path}")

            with open(screenshot_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode("utf-8")

            if hasattr(report,"extras"):
                report.extras.append(pytest_html.extras.png(image_data))
            else:
                report.extras = [pytest_html.extras.png(image_data)]