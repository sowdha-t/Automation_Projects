from sqlite3.dbapi2 import paramstyle

import pytest
from pages.dashboard_page import DashboardPage
from pages.events_page import EventsPage
from utils.json_reader import JsonReader

test_records = JsonReader.read_json("data/search_data.json")
case_ids = [data["test_case"] for data in test_records]

#@pytest.mark.skip
def test_events_are_displayed(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    events_page = EventsPage(logged_in_user)
    dashboard_page.navigate_to_events()
    event_count = events_page.get_event_count()
    assert event_count > 0

@pytest.mark.parametrize("data",test_records,ids=case_ids)
def test_search_events(logged_in_user,data):
    dashboard_page = DashboardPage(logged_in_user)
    events_page = EventsPage(logged_in_user)
    search_text = data["search_text"]
    print(search_text)
    dashboard_page.navigate_to_events()

    if data["result_type"] == "found":
        events_page.search_valid_event(search_text)
        event_names = events_page.get_event_names()
        print(event_names)
        assert len(event_names) > 0
        assert all(search_text.lower() in name.lower() for name in event_names)
    elif data["result_type"] == "not_found":
        event_found = events_page.search_invalid_event(search_text)
        assert event_found
        assert events_page.get_no_events_message() == data["expected_result"]







