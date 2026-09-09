from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from utils.json_reader import JsonReader
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage

@pytest.fixture(scope='function')
def driver():
    config = ConfigReader.get_config()
    #set-up: Initializing Chrome via Webdriver Manager Automatically
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome(service=service, options=options)
    login_url = config["base_url"] + config["login_url"]
    driver.get(login_url)

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def logged_in_user(driver):
    # Read login test data
    test_records = JsonReader.read_json( "data/local/login_data.json" )
    # Find the valid login record
    valid_login_data = next( data for data in test_records if data["expected_result"] == "success" )
    # Perform login
    login_page = LoginPage(driver)
    login_page.login_to_eventhub( valid_login_data["email"], valid_login_data["password"] )
    # Return the browser after successful login
    return driver


