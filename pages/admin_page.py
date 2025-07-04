# Admin code to perform add new user and validate new user

# Importing By to locate web elements using locators like XPATH
from selenium.webdriver.common.by import By

# Importing WebDriverWait for explicit wait handling
from selenium.webdriver.support.ui import WebDriverWait

# Importing expected conditions for wait conditions like element clickability, visibility, etc.
from selenium.webdriver.support import expected_conditions as EC

# Importing exception classes to handle common Selenium errors
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

# Importing Keys class to simulate keyboard actions like arrow down and enter
from selenium.webdriver.common.keys import Keys

# Importing sleep to add fixed delays for UI to load or stabilize
from time import sleep

# Importing locators from external file to maintain cleaner code and separation of concerns
from locators.locators import Locators

# Creating AdminPage class to define admin-related actions like add user, check user, etc.
class AdminPage:
    # Initializing driver and WebDriverWait instance
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to add a new user from the Admin panel
    def add_user(self):
        try :
            # Log starting point
            print("new user creation test")
            # Click the Admin menu from sidebar
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.ADMIN_MENU))).click()
            print("admin menu clicked")
            # Click the Add User button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.ADD_USER_BUTTON))).click()
            print("add user clicked ")
            sleep(5)
            # Wait for the user role dropdown and click it
            user_role_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.USER_ROLE_DROPDOWN)))
            user_role_dropdown.click()
            # Use JavaScript click for better reliability
            self.driver.execute_script("arguments[0].click();", user_role_dropdown)
            sleep(1)
            # Select user role via keyboard (arrow down + enter)
            user_role_dropdown.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("user role selected")
            sleep(2)
            # Locate employee name input and type it
            user_name = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.EMPLOYEE_NAME_INPUT)))
            user_name.send_keys("Melissa  Cassin")
            # Use JavaScript click for stability
            self.driver.execute_script("arguments[0].click();", user_name)
            sleep(1)
            # Select from dropdown suggestions
            user_name.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("entered employee name")
            sleep(5)
            # Locate and click the status dropdown
            status_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.STATUS_DROPDOWN)))
            status_dropdown.click()
            # Use JS click for safety
            self.driver.execute_script("arguments[0].click();", status_dropdown)
            sleep(1)
            # Select status via keyboard
            status_dropdown.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("user status selected")
            sleep(5)
            # Enter new username
            self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.USERNAME_INPUT))).send_keys("samzo")
            sleep(2)
            print("username entered : samzo")
            # Enter password
            self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.PASSWORD_INPUT))).send_keys("Samzo12")
            sleep(2)
            print("password entered: Samzo12")
            # Enter confirm password
            self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.CONFIRM_PASSWORD_INPUT))).send_keys("Samzo12")
            sleep(2)
            print("confirm password entered: Samzo12")
            # Click the save button to create the user
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.SAVE_BUTTON))).click()
            sleep(2)
            print("save button clicked")
        # Catch and log any exception that occurs during the user creation
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("new user couldnt be created",e)

    # Method to verify that the new user appears in the admin management table
    def check_new_user(self) :
        try :
            # Log the start of check
            print("checking the new user")
            # Click the Admin menu
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.ADMIN_MENU))).click()
            print("admin menu clicked")
            sleep(5)
            # Enter the username to search
            self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.USER_INPUT))).send_keys("samzo")
            print("username entered")
            # Enter the full employee name for validation
            user_name_validation = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.NAME_INPUT)))
            user_name_validation.send_keys("Melissa  Cassin")
            # Use JS click to select the suggestion
            self.driver.execute_script("arguments[0].click();", user_name_validation)
            sleep(1)
            # Select from suggestion using keyboard
            user_name_validation.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("name entered")
            # Click the search button (which is reusing SAVE_BUTTON locator)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.SAVE_BUTTON))).click()
            print("search button clicked") 
            try :
                # Try to locate user in the table
                check_user_input = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.CHECK_USER_INPUT)))
                check_user_input.is_displayed() 
                print("new user name is displayed in the management data")
            # Handle user not found inside inner try
            except :
                print("couldnt find user name in management data")
            return True    
        # Catch and log outer exceptions during search
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("new user couldnt be found in management data",e)
            return False
