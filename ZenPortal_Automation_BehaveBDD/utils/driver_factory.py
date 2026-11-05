from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class DriverFactory:

    @staticmethod
    def get_driver(browser_name, headless=False):
        browser_name = browser_name.lower()

        if browser_name == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")

            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Chrome(options=options)

            if not headless:
                driver.maximize_window()

            return driver

        elif browser_name == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            driver = webdriver.Firefox(options=options)

            if not headless:
                driver.maximize_window()

            return driver
            # Edge
        elif browser_name == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")

            options.add_argument("--window-size=1920,1080")

            driver = webdriver.Edge(
                options=options
            )

            if not headless:
                driver.maximize_window()

            return driver

        raise ValueError(
            f"Unsupported browser: {browser_name}"
        )
