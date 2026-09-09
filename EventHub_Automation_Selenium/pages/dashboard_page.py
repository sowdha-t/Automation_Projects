from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    #Locators needed for the Dashboard page

    #Top Menu links
    __eventhub_main_dashboard_link = (By.LINK_TEXT, "EventHub")
    __home_nav_menu = (By.LINK_TEXT, "Home")
    __events_nav_menu = (By.ID, "nav-events")
    __mybookings_nav_menu = (By.ID, "nav-bookings")
    __apidocs_nav_menu = (By.LINK_TEXT, "API Docs")
    __admin_nav_menu = (By.XPATH, "//div[@class='relative']/button")
    __manage_events_nav_menu = (By.LINK_TEXT, "Manage Events")
    __manage_bookings_nav_menu = (By.LINK_TEXT, "Manage Bookings")
    __user_email = (By.ID, "user-email-display")
    __logout_nav_menu = (By.ID, "logout-btn")

    #Centre Page Buttons
    __browse_events_button = (By.LINK_TEXT, "Browse Events →")
    __mybookings_button =  (By.XPATH, "//button[text()='My Bookings']")

    #Featured Events Section Card
    __view_all_event_cards = (By.LINK_TEXT, "View all →")
    __featured_events_list = (By.CSS_SELECTOR, "[data-testid='event-card']") #Returns list of events displayed in the page
    __featured_events_booknow_button_list = (By.CSS_SELECTOR, "[data-testid='book-now-btn']") #Returns the list of all book now buttons in the Featured Event list

    #Explore all events button at the bottom of the dashboard page
    __explore_all_events_button = (By.XPATH, "//button[text()='Explore All Events']")

    def get_user_email(self):
        return self.get_text(self.__user_email)

    def navigate_to_events(self):
        self.click_element(self.__events_nav_menu)
        self.wait_for_url_contains("/events")

    def navigate_to_my_bookings(self):
        self.click_element(self.__mybookings_nav_menu)
        self.wait_for_url_contains("/bookings")
