from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from utils.config_reader import ConfigReader


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
