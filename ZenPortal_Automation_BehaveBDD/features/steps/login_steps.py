from behave import given, when, then
from pages.login_page import LoginPage
import time

@given('user navigate to the Zen Portal login page')
def navigate(context):
    context.login_page = LoginPage(context.driver)
    base_url = context.settings.get("settings","base_url")
    context.login_page.navigate_to_url(base_url)

@then('verify that the username input box is visible')
def verify_username_visible(context):
    is_visible = context.login_page.verify_email_present()
    assert is_visible is True, "Username field is not visible"

@then('verify that the password box is visible')
def verify_password_visible(context):
    is_visible = context.login_page.verify_password_present()
    assert is_visible is True, "Password field is not visible"

@then('verify that submit button is visible')
def verify_submit_button_visible(context):
    is_visible = context.login_page.verify_submit_button_present()
    assert is_visible is True, "Submit button is not visible"

#--------------------Successful Login------------------------------------------
@when('user enter valid configured credentials')
def verify_successful_login(context):
    username = context.valid_email
    password = context.valid_password
    print(context.valid_email,context.valid_password)
    context.login_page.login_to_portal(username,password)

@when('click on the submit button')
def submit_login_button(context):
    context.login_page.submit_login()

@then('validate user logged into the dashboard page')
def user_navigated_to_dashboard(context):
    current_url = context.login_page.get_current_url()
    assert "dashboard" in current_url.lower() or "zenclass" in current_url.lower()
    dashboard_header = context.login_page.verify_dashboard_header()
    assert dashboard_header == "Dashboard"

#-------------------Logout functionality-------------------------
@given('user in the dashboard page')
def user_in_dashboard(context):
    username = context.valid_email
    password = context.valid_password
    context.login_page.login_to_portal(
       username,password
    )
    context.login_page.submit_login()


@when('user click the profile menu and click log out')
def logout(context):
    context.login_page.logout()


@then('user is redirected back to the login page')
def verify_logout(context):
    context.login_page.wait_for_url_contains("login")
    print(f"url :{context.login_page.get_current_url()}")
    assert "login" in context.login_page.get_current_url().lower()


#-----------------------Invalid Credentials Login steps----------
@when('user enter invalid "{username}" and "{password}"')
def verify_unsuccessful_login(context,username,password):
    if username == '""':
        username = ""
    if password == '""':
        password = ""
    context.login_page.login_to_portal(username, password)

@then('appropriate "{error_message}" is displayed in "{error_field}"')
def verify_error_message(context,error_message,error_field):
    print(f"Inside verify_error_message:{error_message}")
    expected_error_message = error_message

    if expected_error_message:
        actual = context.login_page.get_error_message(error_field)
        print(f"Actual error message:{actual}")
        assert actual == expected_error_message , (
            f"[expected '{expected_error_message}' "
            f"under the {error_field} field but found '{actual}'"
        )

@then("the user remains on the login page")
def verify_still_on_login(context):
    context.login_page.wait_for_url_contains("login")
    print(f"url :{context.login_page.get_current_url()}")
    assert "login" in context.login_page.get_current_url()


