from pytest_bdd import given, when, then, scenarios
import pytest

from pages.home_page import HomePage

#Links all scenarios in the feature file to the steps below
scenarios('../features/home_page.feature')


@given("the user opens the Guvi Home Page")
def navigate_to_home_page(driver,base_url):
    url = "https://www.guvi.in"
    home_page = HomePage(driver)
    print(base_url)
    home_page.load_home_page(base_url)

@then("the application should load without errors")
def verify_successful_navigation(driver):
    home_page = HomePage(driver)
    print(home_page.get_page_title())
    assert "HCL" in home_page.get_page_title() , "Home page Title is empty"
    assert "guvi.in" in home_page.get_home_page_url()
