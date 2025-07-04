# OrangeHRM Application - Automation Testing Framework


## Project Objective

**This project focuses on automated testing of the HR management web application OrangeHRM, aiming to validate core functionalities like login, 
user management, menu navigation, and logout. Using Selenium with Pytest and the Page Object Model, the framework simulates real-world user 
actions including form submissions and navigation workflows. The test suite covers both positive and negative test scenarios, with detailed logging
and result reporting. Cross-browser compatibility is ensured by running tests on multiple browsers. Explicit waits are implemented for better 
synchronization with UI events, making the framework reliable, maintainable, and suitable for continuous regression testing.**

## Scope
**The automation is designed to perform cross-browser validation across commonly used web browsers (e.g., Chrome, Firefox, Edge, Safari). 
The system will interact with the web elements and execute test cases covering both positive and negative scenario essential for the website**

## 🔧 Tech Stack
- Selenium
- Pytest
- Page Object Model (POM)
- Python
- openpyxl

## 📁 Folder Structure
```
Project-2/
├── data/
│   └── test_data.xlsx
├── locators/
│   └── locators.py
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── admin_page.py
├── Reports/
│   ├── hrm_report.html
│   ├── hrm_report2.html
│   ├── hrm_report3.html
│   └── hrm_report4.html
├── tests/
│   └── test_hrm.py
├── utilities/
│   ├── environment_setup.py
│   ├── excel_reader.py
│   └── excel_writer.py
└── requirement.py

```

- pages/: Page classes for modular automation
- locators/: Centralized locator storage
- reports/: Storing the results
- data/: Test data
- tests/: Test cases
- utilities/: reading and writing excel data,Fixtures and setup
 


## 🔩 Features
- Cross-browser compatible (with browser driver setup)
- Positive and negative login test cases
- UI element verification for dashboard and login
- Leave, claim, create user
- Page redirection and logout testing

## Test Case Discription

| **Test Name**                     | **Description**                                                                       |
| ----------------------------------| ------------------------------------------------------------------------------------- |
| test_home_url_accessibility       | Verifies that the OrangeHRM login page URL is accessible.                             |
| test_login_fields_visibility      | Checks if the username and password fields and login button are functional.           |
| test_forgot_password_link         | Validates the "Forgot Password" flow and checks for successful message popup.         |
| test_main_menu_clickable          | Ensures all main dashboard menus (Admin, PIM, Leave, etc.) are clickable.             |
| test_myinfo_submenus              | Verifies visibility and accessibility of My Info > Personal, Contact, Emergency tabs. |
| test_create_and_login_user        | Creates a new user and verifies successful login with that user.                      |
| test_validate_new_user            | Confirms the newly created user is listed in the Admin > User Management table.       |
| test_user_claim                   | Logs in with newly created user and verifies the claim creation process.              |
| test_assign_leave                 | Assigns leave for an employee and verifies the process is successful.                 |
| test_login_with_valid_and_invalid | Data-driven test that logs in with both valid and invalid credentials from Excel.     |



## How to run 
To execute the automated test suite and generate reports, follow the steps below:

1. **Install dependencies** (if not already installed): From the requirement.py by pip install -r requirement.py
2. **Run all test cases and generate a full HTML report** : pytest TestScript/testscript.py -d -s --html=Reports/report.html
   If the test cases have inconsistent fails and errors you can try with the below steps to avoid hassel 
          **Run all test cases and generate a full report**: pytest TestScript/testscript.py::<individual test name> -v -s --json-report --html=Reports/report.html
         

## Test Results

![Test Screenshot](https://github.com/sakshinitnaware/Python-Project-2/blob/main/Reports/TestScreenshort1.PNG)
![Test Screenshot](https://github.com/sakshinitnaware/Python-Project-2/blob/main/Reports/TestScreenshort2.PNG)
![Test Screenshot](https://github.com/sakshinitnaware/Python-Project-2/blob/main/Reports/TestScreenshort3.PNG)
![Test Screenshot](https://github.com/sakshinitnaware/Python-Project-2/blob/main/Reports/TestScreenshort4.PNG)
