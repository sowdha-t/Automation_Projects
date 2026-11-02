import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from utils.config_reader import ConfigReader
from pages.home_page import HomePage

load_dotenv() #read values from .env file

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://www.guvi.in")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    reader = ConfigReader()
    return reader

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