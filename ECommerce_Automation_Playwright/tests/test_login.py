from playwright.sync_api import expect
from config.settings import VALID_USERNAME, VALID_PASSWORD

def test_application_launch(login_page):
    login_page.navigate("/")
    expect(login_page.page).to_have_title("Swag Labs")

def test_successful_login(login_page):
    login_page.navigate("/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    expect(login_page.page).to_have_title("Swag Labs")
    expect(login_page.page).to_have_url("inventory.html")
    expect(login_page.page.locator(".title")).to_have_text("Products")



