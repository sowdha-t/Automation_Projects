import pytest
import time

from pages.dashboard_page import DashboardPage
from pages.events_page import EventsPage
from utils.json_reader import JsonReader

test_records = JsonReader.read_json("data/search_data.json")

#Filtering the test_records for category based search and city based search and text based search

text_filter_data = [data for data in test_records if data["test_case"] == "Search Text"]

category_filter_data = [data for data in test_records if data["test_case"] == "Category Based Search"]
category_case_ids = [data["test_case_name"] for data in category_filter_data]

category_dropdown_data = [data for data in test_records if data["test_case"] == "Category Recursive check"]

city_filter_data = [data for data in test_records if data["test_case"] == "City Based Search"]
city_case_ids = [data["test_case_name"] for data in city_filter_data]

#@pytest.mark.skip
def test_events_are_displayed(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    event_count = events_page.get_event_count()
    assert event_count > 0

#@pytest.mark.skip
@pytest.mark.parametrize("data",text_filter_data,ids=lambda data : data["test_case_name"])
def test_search_events(logged_in_user,data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    search_text = data["search_text"]
    print(search_text)
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


#@pytest.mark.skip
@pytest.mark.parametrize("category_data",category_filter_data,ids=lambda data : data["test_case_name"])
def test_search_category(logged_in_user,category_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    search_option = category_data["search_option"]
    #events_page.navigate_to_events_page()
    #category_check = events_page.category_based_search(search_option)

    if category_data["result_type"] == "found":
        category_check = events_page.category_based_search(search_option)
        assert category_check, f"Some events do not belong to the category:{search_option}"

    elif category_data["result_type"] == "not_found":
        category_check = events_page.category_based_search(search_option)
        assert not category_check
        assert events_page.get_no_events_message() == category_data["expected_result"]


@pytest.mark.parametrize("category_dropdown_data",category_dropdown_data,ids=lambda data: data["test_case_name"])
def test_verify_all_dropdown_category_search(logged_in_user,category_dropdown_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    print("Test event page:Category dropdown values to test",category_dropdown_data["category_values_to_test"])
    actual_results = events_page.verify_all_dropdown_category_search(category_dropdown_data["category_values_to_test"])
    print(actual_results)

    expected_results = category_dropdown_data["expected_results"]

    #verify that every dropdown selection produced a result
    assert len(actual_results) == len(expected_results), (f"Expected {len(expected_results)} results but received {len(actual_results)}")

    #Verify each observed result
    for actual, expected in zip(actual_results,expected_results):
        assert (actual["result_type"] == expected), (
            f"Unexpected result for category "  
            f"'{actual['selected_value']}'. " 
            f"Expected: {expected}, " 
            f"Actual: {actual['result_type']}" )

        # For categories that should return events
        if actual["result_type"] == "found":
            if actual["selected_value"] != "":
                assert all(
                    category == actual["selected_value"]
                    for category in actual["actual_categories"]
                ), ( f"Unexpected categories for " 
                     f"'{actual['selected_value']}': " 
                     f"{actual['actual_categories']}"
                     )
            # Verify that All Categories displays multiple categories
            else: assert len(set(actual["actual_categories"])) > 1, (
                "All Categories should display events " 
                "from multiple categories" )
            # Verify that categories expected to return no results
        else:
            assert actual["actual_categories"] == [], (
                f"Expected no categories for " 
                f"'{actual['selected_value']}', " 
                f"but received {actual['actual_categories']}"
            )

@pytest.mark.skip
@pytest.mark.parametrize("city_data",city_filter_data,ids=lambda data : data["test_case"])
def test_search_city(logged_in_user,city_data):
    pass





