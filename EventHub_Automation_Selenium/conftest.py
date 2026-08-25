from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope='function')
def driver():
    #set-up: Initializing Chrome via Webdriver Manager Automatically
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://eventhub.rahulshettyacademy.com/login')

    yield driver

    driver.quit()
