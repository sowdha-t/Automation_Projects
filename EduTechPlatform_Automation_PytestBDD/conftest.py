import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from pages.home_page import HomePage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
                     default=ConfigReader().get("settings", "browser"),
                     help="chrome | firefox | edge | safari")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run without opening a browser window")

@pytest.fixture(scope="function")
def driver(request):
    """Starts a browser before each test and always closes it afterwards."""
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    driver = None
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    return ConfigReader()

@pytest.fixture(scope="session")
def base_url(config):
    return config.get("urls","base_url")

@pytest.fixture(scope="session")
def login_url(config):
    return config.get("urls","login_url")

@pytest.fixture(scope="session")
def register_url(config):
    return config.get("urls","signup_url")

@pytest.fixture(scope="function")
def home_page(driver):
    return HomePage(driver)

@pytest.fixture(scope="function")
def login_page(driver):
    return LoginPage(driver)

load_dotenv() #read values from .env file

@pytest.fixture(scope="session")
def valid_credentials():
    valid_email = os.getenv("GUVI_EMAIL")
    valid_pswd = os.getenv("GUVI_PASSWORD")
    if not valid_email or not valid_pswd:
        pytest.fail("valid email and pswd credentials are missing in .env file")
    return valid_email,valid_pswd