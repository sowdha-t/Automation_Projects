from pathlib import Path
import allure
from selenium import webdriver
from utils.config_reader import ConfigReader
import shutil
from dotenv import load_dotenv
import os

from utils.driver_factory import DriverFactory

load_dotenv()

def before_all(context):
    #setting the environment variables
    context.valid_email = os.getenv("valid_username")
    context.valid_password = os.getenv("valid_password")
    results_dir = Path("reports/allure-results")

    if results_dir.exists():
        print("Cleaning Allure Results Folder...")
        shutil.rmtree(results_dir)

    results_dir.mkdir(parents=True, exist_ok=True)
    context.settings = ConfigReader()

def before_scenario(context, scenario):
    browser = context.settings.get(
        "settings",
        "browser"
    ).lower()
    headless = context.settings.get_bool(
        "settings",
        "headless"
    )
    context.driver = DriverFactory.get_driver(browser,headless)
    allure.dynamic.label(browser)
    tags = scenario.tags
    print(tags)

    if "blocker" in tags:
        allure.dynamic.severity(allure.severity_level.BLOCKER)
    elif "critical" in tags:
        allure.dynamic.severity(allure.severity_level.CRITICAL)
    elif "normal" in tags:
        allure.dynamic.severity(allure.severity_level.NORMAL)
    elif "minor" in tags:
        allure.dynamic.severity(allure.severity_level.MINOR)


def after_scenario(context, scenario):
    print(scenario.status)
    if scenario.status == "failed" or scenario.status == "error":
        screenshot = context.driver.get_screenshot_as_png()
        #Attach it to allure report
        allure.attach(screenshot, name="screenshot_on_failure",attachment_type=allure.attachment_type.PNG)
    if hasattr(context,'driver'):
        context.driver.quit()

