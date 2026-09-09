from pages.dashboard_page import DashboardPage
from utils.json_reader import JsonReader

#Read Login Test Data
test_records = JsonReader.read_json("data/local/login_data.json")

#Fetch only the valid login data
valid_login_data = next(
    data for data in test_records
    if data["expected_result"] == "success"
    )


def test_dashboard_user_email(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    actual_email = dashboard_page.get_user_email()
    assert actual_email == valid_login_data["email"]

def test_dashboard_navigate_to_events(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    print(logged_in_user.current_url)
    assert "/events" in logged_in_user.current_url


def test_dashboard_navigate_to_bookings(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_my_bookings()
    print(logged_in_user.current_url)
    assert "/bookings" in logged_in_user.current_url
