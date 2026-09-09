from pages.dashboard_page import DashboardPage
from pages.events_page import EventsPage

def test_events_are_displayed(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    events_page = EventsPage(logged_in_user)

    dashboard_page.navigate_to_events()
    event_count = events_page.get_event_count()
    event_names = events_page.get_event_names()
    print(event_names)
    assert event_count > 0



