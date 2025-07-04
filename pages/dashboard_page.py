# dashboard code to check menus, assign leave, my info section, claim and logout

# Import By for locating elements using XPATH, ID, etc.
from selenium.webdriver.common.by import By

# Import WebDriverWait to implement explicit waits
from selenium.webdriver.support.ui import WebDriverWait

# Import expected conditions to wait for element visibility, clickability, etc.
from selenium.webdriver.support import expected_conditions as EC

# Import Selenium exceptions for robust error handling
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException

# Import Keys to simulate keyboard actions like ARROW_DOWN or ENTER
from selenium.webdriver.common.keys import Keys

# Import sleep to introduce hard waits (useful in some dynamic UIs)
from time import sleep

# Import Locators class where all XPATHs are defined
from locators.locators import Locators

# DashboardPage class for all dashboard interactions
class DashboardPage:
    # Initialize with driver and wait object
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Method to check and click main menu items
    def main_menu(self) :
        try :
            print("starting the menu items test case")
            # Wait and validate admin menu
            admin_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ADMIN_MENU)))
            if admin_menu.is_displayed() :
                admin_menu.click()
                print("admin menu clicked")
            # Wait and validate PIM menu
            pim_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PIM__MENU)))
            if pim_menu.is_displayed() :
                pim_menu.click()
                print("pim menu clicked")
            # Wait and validate Leave menu
            leave_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.LEAVE_MENU)))
            if leave_menu.is_displayed() :
                leave_menu.click()
                print("leave menu clicked")
            # Wait and validate Time menu
            time_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.TIME_MENU)))
            if time_menu.is_displayed() :
                time_menu.click()
                print("time menu clicked")
            # Wait and validate Recruitment menu
            recruitmen_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.RECRUITMENT_MENU)))
            if recruitmen_menu.is_displayed() :
                recruitmen_menu.click()
                print("recruitmen menu clicked")
            # Wait and validate My Info menu
            myinfo_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.MYINFO_MENU)))
            if myinfo_menu.is_displayed() :
                myinfo_menu.click()
                print("my info menu clicked")
            # Wait and validate Performance menu
            performance_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PERFORMANCE_MENU)))
            if performance_menu.is_displayed() :
                performance_menu.click()
                print("performance menu clicked")
            # Wait and validate Dashboard menu
            dashboard_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.DASBOARD_MENU)))
            if dashboard_menu.is_displayed() :
                dashboard_menu.click()
                print("dashboard menu clicked")
            print("All menu items are visible and redirected to respective pagaes")
            # Return True if all menus processed
            return True 
        # Exception handling for all types of Selenium errors
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("Cant find menus", e)
            return False

    # Method to assign leave to a specific employee
    def assign_leave(self):
        try :
            print("assign leave test")
            # Click Leave menu
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.LEAVE_MENU))).click()
            print("Leave menu clicked")
            sleep(5)
            # Click Assign Leave
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.ASSIGN_LEAVE))).click()
            print("assign leave clicked")
            sleep(2)
            # Enter employee name
            employee_name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.EMPLOYEE_NAME_INPUT)))
            employee_name.send_keys("James  Butler")
            print("employee name entered")
            sleep(2)
            self.driver.execute_script("arguments[0].click();", employee_name)
            sleep(1)
            employee_name.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            # Select leave type
            leave_type_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.LEAVE_TYPE)))
            leave_type_dropdown.click()
            self.driver.execute_script("arguments[0].click();", leave_type_dropdown)
            sleep(1)
            leave_type_dropdown.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("leave_type_dropdown selected")
            sleep(2)
            # Enter leave start date
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.FROM_DATE))).send_keys("2025-10-09")
            print("entered from leave date")
            sleep(2)
            # Click Save
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.SAVE_BUTTON)))
            save_button.click()
            print("save button clicked")
            # Handle optional confirmation pop-up
            try:
                pop_up = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.POP_UP)))
                pop_up.click()
                print("Pop-up clicked")
            except TimeoutException:
                print("Pop-up did not appear after saving")

            print("Leave assignment process completed")
            return True
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("cant asseign leave", e)
            return False

    # Method to verify various sub-sections in My Info
    def verify_myinfo_sections(self):
        try :
            # Click My Info menu
            self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.MYINFO_MENU))).click()
            sleep(5)
            # Click Personal Details section
            personal_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PERSONAL_DETAILS)))
            personal_field.click()
            print("personal field clicked")
            # Click Contact Details section
            contact_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.CONTACT_DETAILS)))
            contact_field.click()
            print("contact field clicked")
            # Click Emergency Contacts section
            emergency_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.EMERGENCY_CONTACTS)))
            emergency_field.click()
            print("emergency field clicked")
            return True
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("my info not present", e)

    # Method to assign a claim for an employee
    def assign_calim(self):
        try :
            print("assign claim test")
            # Click Claim menu
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CLAIM_MENU))).click()
            print("claim menu clicked")
            sleep(5)
            # Click Assign Claim
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.ASSIGN_CLAIM))).click()
            print("assign claim clicked")
            sleep(2)
            # Enter employee name
            employee_name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.EMPLOYEE_NAME_INPUT)))
            employee_name.send_keys("James  Butler")
            print("employee name entered")
            sleep(2)
            self.driver.execute_script("arguments[0].click();", employee_name)
            sleep(1)
            employee_name.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            # Select event type
            event_type_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.EVENT_TYPE)))
            event_type_dropdown.click()
            sleep(1)
            self.driver.execute_script("arguments[0].click();", event_type_dropdown)
            sleep(2)
            event_type_dropdown.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("event_type_dropdown selected")
            sleep(2)
            # Select currency type
            currency_type_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CURRENCY_TYPE)))
            currency_type_dropdown.click()
            sleep(1)
            # Select INR
            indian_currency_type = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.INDIAN_CURRENCY)))
            indian_currency_type.click()
            self.driver.execute_script("arguments[0].click();", currency_type_dropdown)
            sleep(2)
            currency_type_dropdown.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
            print("indian currency selected")
            sleep(2)
            # Click Create Claim button
            claim_create_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CLAIM_CREATE_BUTTON)))
            claim_create_button.click()
            print("clain button clicked")
            return True
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("cant asseign leave", e)
            return False

    # Method to log out from the application
    def logout(self):
        try :
            print("logging out")
            # Click profile dropdown
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.LOGOUT_DROPDOWN))).click()
            # Click Logout button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.LOGOUT_BUTTON))).click()
            print("loged out")
        except (NoSuchElementException, TimeoutException, ElementNotInteractableException, Exception) as e :
            print("cant asseign leave", e)
