import pytest

from pages.add_event_page import AddEventPage
from pages.dashboard_page import DashboardPage
from pages.events_page import EventsPage
from utils.json_reader import JsonReader

test_records = JsonReader.read_json("data/add_event_data.json")

test_case_ids = [data["test_case_name"] for data in test_records]

@pytest.mark.smoke
@pytest.mark.parametrize("event_creation_data",test_records,ids=test_case_ids)
def test_add_new_event(logged_in_user,event_creation_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    events_page.navigate_to_add_event()
    add_event_page = AddEventPage(logged_in_user)
    message = add_event_page.create_new_event(event_creation_data)

    assert message == "Event created!", (
        f"Event creation failed. Notification: {message}")
