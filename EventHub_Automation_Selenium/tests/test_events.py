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

verify_filter_data = [data for data in test_records if data["test_case"] == "Verify Clear Filters"]

combined_filter_search = [data for data in test_records if data["test_case"] == "Combined City and Category Search"]

#@pytest.mark.skip
@pytest.mark.smoke
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

@pytest.mark.smoke
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


@pytest.mark.parametrize("city_data",city_filter_data,ids=lambda data : data["test_case_name"])
def test_search_city(logged_in_user,city_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    search_option = city_data["search_option"]

    if city_data["result_type"] == "found":
        city_check = events_page.city_based_search(search_option)
        assert city_check, f"Some events do not belong to the city:{search_option}"

    elif city_data["result_type"] == "not_found":
        city_check = events_page.city_based_search(search_option)
        assert not city_check
        assert events_page.get_no_events_message() == city_data["expected_result"]


@pytest.mark.parametrize("verify_filter_data",verify_filter_data,ids=lambda data : data["test_case_name"])
def test_clear_filter_functionality(logged_in_user,verify_filter_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)

    results = events_page.verify_clear_filter_functionality(
        search_text=verify_filter_data["search_text"],
        category=verify_filter_data["category"],
        city= verify_filter_data["city"])
    print(results)

    # Verify search filter
    search_result = results["search_filter"]

    assert search_result["button_visible_after_filter"], (
        "Clear Filters button did not appear after applying search"
    )

    assert not search_result["button_visible_after_clear"], (
        "Clear Filters button remained visible after clearing search"
    )

    assert search_result["search_value_after_clear"] == "", (
        "Search input was not cleared"
    )

    # Verify category filter
    category_result = results["category_filter"]

    assert category_result["button_visible_after_filter"], (
        "Clear Filters button did not appear after selecting category"
    )

    assert not category_result["button_visible_after_clear"], (
        "Clear Filters button remained visible after clearing category"
    )

    assert category_result["category_value_after_clear"] == "", (
        "Category dropdown did not reset to All Categories"
    )

    # Verify city filter
    city_result = results["city_filter"]

    assert city_result["button_visible_after_filter"], (
        "Clear Filters button did not appear after selecting city"
    )

    assert not city_result["button_visible_after_clear"], (
        "Clear Filters button remained visible after clearing city"
    )

    assert city_result["city_value_after_clear"] == "", (
        "City dropdown did not reset to All Cities"
    )

@pytest.mark.parametrize("combined_filter_search_data",combined_filter_search,ids= lambda data : data["test_case_name"])
def test_verify_combined_filters_search(logged_in_user,combined_filter_search_data):
    dashboard_page = DashboardPage(logged_in_user)
    dashboard_page.navigate_to_events()
    events_page = EventsPage(logged_in_user)
    result = events_page.verify_combined_filter_search(combined_filter_search_data)
    expected = combined_filter_search_data["result_type"]

    # Verify the actual result matches the expected outcome
    assert result["actual_result"] == expected, (
        f"Unexpected result for city '{result['selected_city']}' "
        f"and category '{result['selected_category']}'. "
        f"Expected: {expected}, "
        f"Actual: {result['actual_result']}, "
        f"Message: {result['no_events_message']}"
    )

    if expected == "found":
        assert result["event_count"] > 0, (
            "Expected matching events, but no event cards were returned"
        )

        assert result["category_match"], (
            f"Unexpected categories: {result['actual_categories']}"
        )

        assert result["city_match"], (
            f"Unexpected locations: {result['actual_locations']}"
        )

    else:
        assert result["event_count"] == 0, (
            f"Expected no events, but found "
            f"{result['event_count']} events"
        )

        assert result["no_events_message"] == "No events found", (
            f"Unexpected no-results message: "
            f"{result['no_events_message']}"
        )









