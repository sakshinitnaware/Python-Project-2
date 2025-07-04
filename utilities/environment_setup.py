# environment code to automate the drivers and browser functions 

# Import pytest for defining setup fixtures
import pytest

# Import Selenium WebDriver core
from selenium import webdriver

# Import Chrome driver service
from selenium.webdriver.chrome.service import Service as ChromeService
# Import Firefox driver service
from selenium.webdriver.firefox.service import Service as FirefoxService
# Import Edge driver service
from selenium.webdriver.edge.service import Service as EdgeService

# Import Chrome options for headless mode and other configs
from selenium.webdriver.chrome.options import Options as ChromeOptions
# Import Firefox options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# Import Edge options
from selenium.webdriver.edge.options import Options as EdgeOptions

# Automatically download and manage the correct version of ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
# Automatically download and manage the correct version of GeckoDriver (Firefox)
from webdriver_manager.firefox import GeckoDriverManager
# Automatically download and manage the correct version of EdgeDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Pytest fixture to provide a reusable browser setup for each test function
@pytest.fixture(scope="function")         
def setup():
    # Initialize the driver as None before launching any browser
    driver = None

    try:
        # Try launching Chrome in headless mode with specific arguments
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")  # New headless mode for Chrome
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid /dev/shm size limitations
        chrome_options.add_argument("--window-size=1920,1080")  # Set window size for headless view
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        print("Launched Chrome in headless mode.")
    except Exception as e1:
        # If Chrome fails, print the error and try Firefox
        print("Chrome not available:", e1)
        try:
            # Try launching Firefox in headless mode with specific arguments
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--no-sandbox")
            firefox_options.add_argument("--disable-dev-shm-usage")
            firefox_options.add_argument("--window-size=1920,1080")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
            print("Launched Firefox in headless mode.")
        except Exception as e2:
            # If Firefox fails, print the error and try Edge
            print("Firefox not available:", e2)
            try:
                # Try launching Edge in headless mode with specific arguments
                edge_options = EdgeOptions()
                edge_options.add_argument("--headless=new")
                edge_options.add_argument("--no-sandbox")
                edge_options.add_argument("--disable-dev-shm-usage")
                edge_options.add_argument("--window-size=1920,1080")
                driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
                print("Launched Edge in headless mode.")
            except Exception as e3:
                # If all browsers fail, raise an exception to stop test execution
                print("Edge not available:", e3)
                raise Exception("No supported browser is available in headless mode on this system.")

    # Maximize the browser window (has no effect in headless, but safe to call)
    driver.maximize_window()
    # Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Yield the driver to the test function
    yield driver
    # Close the browser after test execution
    driver.quit()
