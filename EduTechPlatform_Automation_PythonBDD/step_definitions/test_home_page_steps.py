from pytest_bdd import given, when, then, scenarios, parsers

#Links all scenarios in the feature file to the steps below
scenarios('../features/home_page.feature')

@given("the user opens the Guvi Home Page")
def navigate_to_home_page(home_page,base_url):
    print(base_url)
    home_page.load_home_page(base_url)

@then("the application should load without errors")
def verify_successful_navigation(home_page):
    print(home_page.get_page_title())
    assert "HCL" in home_page.get_page_title() , "Home page Title is empty"
    assert "guvi.in" in home_page.get_home_page_url()

@then(parsers.parse('the page title should be "{title}"'))
def verify_page_title(home_page, title):
    assert title == home_page.get_page_title()

@then("the login button should be visible")
def check_login_button_visible(home_page):
    assert home_page.check_login_displayed(), "Login Button is not visible"

@when("the user clicks the login button")
def click_login_button(home_page):
    home_page.click_login_button()
    print(home_page.get_current_url())

@then("the user navigates to login page")
def navigate_to_login_page(home_page):
    home_page.wait_for_url_contains("sign-in")
    assert "sign-in" in home_page.get_current_url()

@then("the sign up button should be visible")
def check_signup_button_visible(home_page):
    assert home_page.check_signup_displayed(), "Sign up button is not displayed"

@when("the user clicks the sign up button")
def click_signup_button(home_page):
    home_page.click_signup_button()
    print(home_page.get_current_url())

@then(parsers.parse('the current url should be "{url}"'))
def navigate_to_signup_page(home_page,url):
    print(home_page.get_current_url())
    print(home_page.get_current_url())
    assert url in home_page.get_current_url()

@then(parsers.parse('the user navigates to "{register_url}" successfully'))
def navigate_to_signup_page(home_page,register_url):
    print(home_page.get_current_url())
    print(home_page.get_current_url())
    assert register_url in home_page.get_current_url()

@then("the register page should load properly")
def verify_successful_navigation(home_page):
    print(home_page.get_page_title())
    assert "HCL GUVI | Sign Up" in home_page.get_page_title()
    assert "register" in home_page.get_current_url()




