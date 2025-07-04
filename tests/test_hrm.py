# Test code to automate test for all the test cases 

# Importing OS module to work with file paths
import os
# Importing sys module to manipulate the Python path
import sys
# Importing pytest for writing and executing test cases
import pytest

# Appending the parent directory to system path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing LoginPage class from the pages package
from pages.login_page import LoginPage
# Importing DashboardPage class from the pages package
from pages.dashboard_page import DashboardPage
# Importing AdminPage class from the pages package
from pages.admin_page import AdminPage

# Importing sleep to add wait time between actions
from time import sleep

# Importing utility functions to read and find data from Excel
from utilities.excel_reader import get_test_data, find_row_number
# Importing utility function to write test result into Excel
from utilities.excel_writer import write_test_result
# Importing the browser setup fixture
from utilities.environment_setup import setup

# Setting Excel file path
excel_path = "data/test_data.xlsx"
# Setting worksheet name
sheet_name = "Sheet1"

# Smoke test to validate homepage URL accessibility
@pytest.mark.smoke
def test_home_url_accessibility(setup):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        assert expected_url == setup.current_url
        print("PASS : URL TEST")

# Sanity test to verify login form fields and functionality
@pytest.mark.sanity  
def test_login_fields_visibility(setup):
        login = LoginPage(setup)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()
        assert "dashboard" in setup.current_url.lower()
        print("PASS : LOGIN FIELDS VISIBLE TEST")

# Smoke test to verify forgot password functionality
@pytest.mark.smoke        
def test_forgot_password_link(setup):
        login = LoginPage(setup)
        assert login.forget_password()
        print("PASS : FORGOT PASSWORD TEST")

# Smoke test to verify main navigation menus are clickable
@pytest.mark.smoke
def test_main_menu_clickable(setup):
        login = LoginPage(setup)
        login.login("Admin", "admin123")
        dashboard = DashboardPage(setup)
        assert dashboard.main_menu()
        print("PASS : MENU ITEMS VISIBLE AND CLICKABLE TEST")

# Smoke test to validate submenus under My Info section
@pytest.mark.smoke
def test_myinfo_submenus(setup):
        login = LoginPage(setup)
        login.login("Admin", "admin123")
        dashboard = DashboardPage(setup)
        assert dashboard.verify_myinfo_sections()
        print("PASS : MY INFO FIELDS VISIBLE AND CLICKABLE TEST")

# Test to create new user and verify login with the new user
def test_create_and_login_user(setup):
        login = LoginPage(setup)
        login.login("Admin", "admin123")
        admin = AdminPage(setup)
        admin.add_user()
        dashboard = DashboardPage(setup)
        dashboard.logout()
        login.login("samzo", "Samzo12")
        assert "dashboard" in setup.current_url.lower()
        print("PASS : NEW USER CREATED AND LOGGED-IN TEST")

# Test to check if newly created user exists in the admin list
def test_validate_new_user(setup):
        login = LoginPage(setup)
        login.login("Admin", "admin123")
        admin = AdminPage(setup)
        admin.add_user()
        sleep(10)
        print("logging out....")
        dashboard = DashboardPage(setup)
        dashboard.logout()
        login.login("Admin", "admin123")
        sleep(5)
        assert admin.check_new_user()
        print("PASS : NEW USER PRESENT IN MANAGEMENT DATA TEST")

# Test to verify assigning claim to a newly created user
def test_user_claim(setup):
        login = LoginPage(setup)
        login.login("Admin", "admin123")
        admin = AdminPage(setup)
        admin.add_user()
        dashboard = DashboardPage(setup)
        dashboard.logout()
        login.login("samzo", "Samzo12")
        assert dashboard.assign_calim()
        print("PASS : USER CALIM TEST")

# Test to validate assigning leave to an employee
def test_assign_leave(setup):
        login = LoginPage(setup)
        login.login("Admin", "admin123")
        dashboard = DashboardPage(setup)
        assert dashboard.assign_leave()
        print("PASS : LEAVE ASSIGN TEST")

# Sanity test for data-driven login using multiple usernames/passwords from Excel
@pytest.mark.sanity
# Parameterizing the test with data from Excel (username, password, expected validity)
@pytest.mark.parametrize("username,password,expected", get_test_data(excel_path, sheet_name))
def test_login_with_valid_and_invalid(setup, username, password, expected):
    # Instantiate LoginPage and perform login
    login = LoginPage(setup)
    login.login(username, password)

    # Find the corresponding row number of the user in Excel for result logging
    row_num = find_row_number(username, excel_path, sheet_name)

    # Check if login was successful by URL check
    is_logged_in = "dashboard" in setup.current_url.lower()

    # Handling logic for expected "valid" login
    if expected == "valid":
        if is_logged_in:
            write_test_result(excel_path, sheet_name, row_num, "PASS")
            DashboardPage(setup).logout()
        else:
            write_test_result(excel_path, sheet_name, row_num, "FAIL")
            assert False, f"Valid user login failed: {username}"
    # Handling logic for expected "invalid" login
    elif expected == "invalid":
        if not is_logged_in:
            write_test_result(excel_path, sheet_name, row_num, "PASS")
        else:
            write_test_result(excel_path, sheet_name, row_num, "FAIL")
            DashboardPage(setup).logout()
            assert False, f"Invalid user unexpectedly logged in: {username}"
