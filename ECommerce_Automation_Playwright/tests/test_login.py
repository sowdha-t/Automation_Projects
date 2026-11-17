import pytest
from playwright.sync_api import expect
from config.settings import VALID_USERNAME, VALID_PASSWORD
from utils.json_reader import JsonReader
from pathlib import Path

json_file_path = Path(__file__).resolve().parent.parent / "data" / "login_data.json"
login_data = JsonReader.read_json(json_file_path)
test_case_ids = [f"TC-01-predefined user name:{data['username']}" for data in login_data]

def test_application_launch(login_page):
    login_page.navigate("/")
    expect(login_page.page).to_have_title("Swag Labs")

def test_successful_login(login_page):
    login_page.navigate("/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    expect(login_page.page).to_have_title("Swag Labs")
    expect(login_page.page).to_have_url("inventory.html")
    expect(login_page.page.locator(".title")).to_have_text("Products")

@pytest.mark.parametrize("login_predefined_users_data",login_data, ids=test_case_ids)
def test_login_with_predefined_users(login_page,
                                     login_predefined_users_data ):
    login_page.navigate("/")
    username = login_predefined_users_data["username"]
    password = VALID_PASSWORD
    expected_result = login_predefined_users_data["expected_result"]
    expected_error_message = login_predefined_users_data.get("expected_error_message","")
    login_page.login(username, password)
    if "success" == expected_result:
        expect(login_page.page).to_have_title("Swag Labs")
        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(login_page.page.locator(".title")).to_have_text("Products")
    elif "failure" == expected_result:
        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(expected_error_message)
    else:
        pytest.fail(f"unsupported expected result:{expected_result}")





