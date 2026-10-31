import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv() #read values from .env file

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://www.guvi.in")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL","empty")