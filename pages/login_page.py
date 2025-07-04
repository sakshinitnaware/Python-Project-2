# login code to perform login functions

# Importing the By class to locate elements using different strategies like XPATH
from selenium.webdriver.common.by import By

# Importing WebDriverWait to apply explicit waits on web elements
from selenium.webdriver.support.ui import WebDriverWait

# Importing expected conditions to wait for elements to be visible, clickable, etc.
from selenium.webdriver.support import expected_conditions as EC

# Importing exceptions to handle various Selenium-related runtime errors
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

# Importing sleep to pause execution temporarily
from time import sleep

# Importing the locators used for finding elements on the page
from locators.locators import Locators


# Defining the LoginPage class to encapsulate all login page operations
class LoginPage:
    # Constructor to initialize WebDriver and WebDriverWait
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to enter the username in the username input field
    def enter_username(self,username):
        try:
            # Wait until the username field is present and enter the provided username
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.USERNAME))).send_keys(username)
            print("entered username")
            return True
        # Handle exceptions that may occur during interaction
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e:
            print("ERROR username field:", e)

    # Method to enter the password in the password input field
    def enter_password(self,password):
        try:
            # Wait until the password field is present and enter the provided password
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.PASSWORD))).send_keys(password)
            print("entered password")
            return True
        # Handle exceptions that may occur during interaction
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e:
            print("ERROR password field:", e)

    # Method to click the login button
    def click_login_button(self):
        try:
            # Wait until the login button is clickable and then click it
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.LOGIN_BUTTON)))
            login_button.click()
            print("login button clicked")
        # Handle exceptions that may occur during the click
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e:
            print("ERROR login button:", e)

    # Method to perform the full login operation (enter username, password, and click login)
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    # Method to handle the forget password functionality
    def forget_password(self) :
        try :
            print("foregt password link test")
            # Print current URL before clicking the link
            print("Current URL:", self.driver.current_url)
            # Click the "Forgot Password" link
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.FORGOT_PASWORD_BUTTON))).click()
            print("link clicked")
            # Print the URL after navigation
            print("Current URL:", self.driver.current_url)
            # Wait for the page to load
            sleep(5)
            print("forget password button clicked")
            # Enter the username or email for reset
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.FOGOT_USERNAME_INPUT))).send_keys("samzo")
            print("entered name")
            # Click the reset button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.RESET_BUTTON))).click()
            print("reset button clicked")
            # Wait for confirmation message to be visible
            sleep(5)
            success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()= 'A reset password link has been sent to you via email.']")))
            # Check if the success message is displayed
            if success_message.is_displayed():
                print("A reset password link has been sent to you via email.")
                return True
            else:
                print("Message element found but not visible.")
                return False
        # Handle any exceptions that may occur during the process
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e:
            print("ERROR login button:", e)
