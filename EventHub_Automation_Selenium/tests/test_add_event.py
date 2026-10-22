import pytest
import time
from pages.add_event_page import AddEventPage
from pages.dashboard_page import DashboardPage
from pages.events_page import EventsPage
from pages.manage_events_page import ManageEventsPage
from utils.json_reader import JsonReader

test_records = JsonReader.read_json("data/add_event_data.json")
update_event_records = JsonReader.read_json("data/update_event_data.json")

test_case_ids = [data["test_case_name"] for data in test_records]


#@pytest.mark.skip
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

    manage_events_page = ManageEventsPage(logged_in_user)

    assert manage_events_page.is_event_displayed_in_table(event_creation_data["event_title"]) ,(
        f"Event {event_creation_data["event_title"]} was not found in the all events table"

    #checking in Events page is pending

    )

#@pytest.mark.skip
@pytest.mark.parametrize("event_title_to_check",["Agentic AI Workshop"],ids=["Event Title Check"])
def test_event_is_displayed_in_admin_table(logged_in_user,event_title_to_check):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    events_page.navigate_to_add_event()
    manage_events_page = ManageEventsPage(logged_in_user)
    #event_title_to_check = "Illaiyaraja Concert"
    assert manage_events_page.is_event_displayed_in_table(event_title_to_check),\
        (f"Given Event Title:{event_title_to_check} is not displayed in the Events table")


#@pytest.mark.skip
@pytest.mark.parametrize("update_event_data",update_event_records,ids=[data["test_case_name"] for data in update_event_records])
def test_update_event(logged_in_user,update_event_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    events_page.navigate_to_add_event()
    add_event_page = AddEventPage(logged_in_user)
    manage_events_page = ManageEventsPage(logged_in_user)
    original_title = update_event_data["event_original_title"]

    #verify original event exist
    assert manage_events_page.is_event_displayed_in_table(original_title), \
        (f"Given Event Title:{original_title}"
         f" is not displayed in the Events table")

    #click edit for the selected event
    manage_events_page.click_edit_event(original_title)
    notification = add_event_page.update_event(update_event_data)
    # Verify successful update
    assert "Event updated!" in notification

    # Verify the updated title in All Events page
    assert manage_events_page.is_event_displayed_in_table(
        update_event_data["event_title"]
    )
    print(update_event_data["event_title"])

    actual_details = manage_events_page.get_event_details(
        update_event_data["event_title"]
    )

    print(actual_details)

    assert actual_details["event_title"] == update_event_data["event_title"]

    assert actual_details["event_city"] == update_event_data["event_city"]

    assert actual_details["event_price"] == update_event_data["event_price"]

    assert actual_details["event_total_seats"].endswith(update_event_data["event_total_seats"])


@pytest.mark.skip
@pytest.mark.parametrize("event_title_to_delete",["Advanced QA Automation Workshop-Updated"],ids=["Event Delete Check Verification"])
def test_delete_event(logged_in_user,event_title_to_delete):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    events_page.navigate_to_add_event()
    manage_events_page = ManageEventsPage(logged_in_user)
    message = manage_events_page.click_delete_event(event_title_to_delete)

    assert message == "Event deleted!", (
        f"Event deletion failed. Notification: {message}")

    assert not manage_events_page.is_event_displayed_in_table(event_title_to_delete), \
        (f"Event {event_title_to_delete} is not deleted successfully")


#@pytest.mark.skip
@pytest.mark.parametrize("event_title_to_delete",["IPL IND Vs AUS Cricket"],ids=["Event Delete Check Verification"])
def test_delete_cancel_event(logged_in_user,event_title_to_delete):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    events_page.navigate_to_add_event()
    manage_events_page = ManageEventsPage(logged_in_user)

    #verifying user clicking the cancel button
    manage_events_page.cancel_delete_event(event_title_to_delete,"cancel_check")
    assert manage_events_page.is_event_displayed_in_table(event_title_to_delete), \
        (f"Event {event_title_to_delete} is deleted")

    #verifying user clicking the close button
    manage_events_page.cancel_delete_event(event_title_to_delete,"close_check")
    assert manage_events_page.is_event_displayed_in_table(event_title_to_delete), \
        (f"Event {event_title_to_delete} is deleted")










