import pytest
from playwright.sync_api import expect
from config.settings import VALID_USERNAME, VALID_PASSWORD
from utils.json_reader import JsonReader
from utils.csv_reader import CSVReader
from pathlib import Path

#Predefined user login data from json file
json_file_path = Path(__file__).resolve().parent.parent / "test_data" / "login_data.json"
login_data = JsonReader.read_json(json_file_path)
test_case_ids = [f"TC-01-predefined user name:{data['username']}" for data in login_data]

#Reading Invalid User login data from CSV file
csv_file_path = Path(__file__).resolve().parent.parent / "test_data" / "invalid_login_data.csv"
invalid_login_user_data_from_csv = CSVReader.read_csv_data(csv_file_path)
invalid_login_test_case_ids =[data['test_case'] for data in invalid_login_user_data_from_csv]


@pytest.mark.skip(reason="Already Passed Test Cases")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_application_launch(login_page):
    login_page.navigate("/")
    expect(login_page.page).to_have_title("Swag Labs")

@pytest.mark.skip(reason="Already Passed Test Cases")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_successful_login(login_page):
    login_page.navigate("/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    expect(login_page.page).to_have_title("Swag Labs")
    expect(login_page.page).to_have_url("inventory.html")
    expect(login_page.page.locator(".title")).to_have_text("Products")


@pytest.mark.skip(reason="Already Passed Test Cases")
@pytest.mark.login
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

@pytest.mark.skip(reason="Already Passed Test Cases")
@pytest.mark.login
@pytest.mark.parametrize("invalid_login_user_data",invalid_login_user_data_from_csv, ids=invalid_login_test_case_ids)
def test_verify_invalid_user_login(login_page,invalid_login_user_data):
    username = invalid_login_user_data["username"]
    password = invalid_login_user_data["password"]
    expected_error_msg = invalid_login_user_data["expected_error"]
    login_page.navigate("/")
    print(username, password, expected_error_msg)
    login_page.login(username, password)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(expected_error_msg)


@pytest.mark.skip(reason="Already Passed Test Cases")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.logout
def test_verify_logout_functionality(login_page,product_page):
    login_page.navigate("/")
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    expect(login_page.page).to_have_title("Swag Labs")
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(login_page.page.locator(".title")).to_be_visible()
    expect(login_page.page.locator(".title")).to_have_text("Products")

    #open menu and click logout
    product_page.open_menu()
    product_page.click_logout()

    #assertions for verifying logout functionality
    expect(login_page.username_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.submit_button).to_be_visible()
    expect(login_page.username_field).to_be_enabled()
    expect(login_page.password_field).to_be_enabled()
    expect(login_page.submit_button).to_be_enabled()
    expect(login_page.page).to_have_url("https://www.saucedemo.com/")










