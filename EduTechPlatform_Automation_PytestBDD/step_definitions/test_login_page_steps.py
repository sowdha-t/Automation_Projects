from pytest_bdd import given,when,then,scenarios,parsers
import time
from utils.csv_reader import get_row
#Links all scenarios in the feature file to the steps below
scenarios('../features/login_page.feature')

@given('the user is on the login page')
def navigate_to(login_page,login_url):
    print(f"sowdha:{login_url}")
    login_page.navigate_to_login_page(login_url)

@when('the user enters valid credentials from configuration')
def check_positive_login_flow(login_page,valid_credentials):
    email_txt, password_txt = valid_credentials
    login_page.enter_login_details(email_txt,password_txt)

@when('the user clicks the submit button')
def submit_login(login_page):
    login_page.submit_login_details()

@then('the user logged in and redirected to dashboard page')
def verify_successful_login(login_page,valid_credentials):
    time.sleep(4)
    email_from_profile = login_page.get_profile_email_details()
    assert email_from_profile == valid_credentials[0]
    print(login_page.get_page_title())
    print(login_page.get_current_url())
    print(email_from_profile)

@when(parsers.parse('the user enters the invalid credentials for test case "{case_id}"'),target_fixture="login_data")
def verify_unsuccessful_login(login_page,case_id, valid_credentials):
    row= get_row("invalid_login_data.csv", case_id)
    email = row["email"]
    password = row["password"]
    if case_id == "wrong_password":
        email = valid_credentials[0]

    login_page.enter_login_details(email ,password)
    print(row)
    return row

@when('the user triggers the validation')
def check_validation_type(login_page,login_data):
    if login_data["validation_type"] == "server_side":
        login_page.submit_login_details()

@then("the expected error message should be displayed")
def verify_error_message(login_page, login_data):
    print(f"Inside verify_error_message:{login_data}")
    field = login_data["error_field"]
    expected_error_message = login_data["error_message"]

    if expected_error_message:
        actual = login_page.get_error_message(login_data["error_field"])
        print(f"Actual error message:{actual}")
        assert actual == login_data["error_message"] , (
            f"[{login_data['validation_type']}] expected '{login_data['error_message']}' "
            f"under the {login_data['error_field']} field but found '{actual}'"
        )
    else:
        assert login_page.is_field_invalid(login_data["error_field"]), f"{field} not marked invalid"


@then("the user remains on the login page")
def verify_still_on_login(login_page):
    assert "sign-in" in login_page.get_current_url()


