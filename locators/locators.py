# Define a class to store all element locators used in the project
class Locators: 
    # XPath for the username input field on login page
    USERNAME = "//input[@name='username']"
    
    # XPath for the password input field on login page
    PASSWORD = "//input[@name='password']"
    
    # XPath for the login button
    LOGIN_BUTTON = "//button[@type='submit']"
    
    # XPath for the "Forgot Password" link on login page
    FORGOT_PASWORD_BUTTON = "//p[contains(@class, 'orangehrm-login-forgot-header')]"
    
    # XPath for the username field in the forgot password form
    FOGOT_USERNAME_INPUT = "//input[@name='username']"
    
    # XPath for the reset button in the forgot password form
    RESET_BUTTON = "//button[@type='submit']"
    
    # XPath for the Admin menu in the main navigation
    ADMIN_MENU = "//span[text()='Admin']"
    
    # XPath for the PIM menu in the main navigation
    PIM__MENU = "//span[text()='PIM']"
    
    # XPath for the Leave menu in the main navigation
    LEAVE_MENU = "//span[text()='Leave']"
    
    # XPath for the Time menu in the main navigation
    TIME_MENU = "//span[text()='Time']"
    
    # XPath for the Recruitment menu in the main navigation
    RECRUITMENT_MENU = "//span[text()='Recruitment']"
    
    # XPath for the My Info menu in the main navigation
    MYINFO_MENU = "//span[text()='My Info']"
    
    # XPath for the Performance menu in the main navigation
    PERFORMANCE_MENU = "//span[text()='Performance']"
    
    # XPath for the Dashboard menu in the main navigation
    DASBOARD_MENU = "//span[text()='Dashboard']"
    
    # XPath for the Claim menu in the main navigation
    CLAIM_MENU = "//span[text()='Claim']"
    
    # XPath for the user dropdown menu (used for logout)
    LOGOUT_DROPDOWN = "//span[@class='oxd-userdropdown-tab']"
    
    # XPath for the logout button inside the user dropdown
    LOGOUT_BUTTON = "//a[text()='Logout']"

    # XPath for the Add User button in the Admin > User Management section
    ADD_USER_BUTTON = "//button[normalize-space()='Add']"
    
    # XPath for the User Role dropdown field (absolute path)
    USER_ROLE_DROPDOWN = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    
    # XPath for the employee name input field
    EMPLOYEE_NAME_INPUT = "//input[@placeholder='Type for hints...']"
    
    # XPath for the Status dropdown field (absolute path)
    STATUS_DROPDOWN = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]"
    
    # XPath for the username input when creating a new user
    USERNAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    
    # XPath for the password input field when creating a new user
    PASSWORD_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    
    # XPath for the confirm password input field when creating a new user
    CONFIRM_PASSWORD_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    
    # XPath for the Save button to submit a form (e.g., create user or leave/claim)
    SAVE_BUTTON = "//button[@type='submit']" 
    
    # XPath for the username search input in Admin > User Management
    USER_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"
    
    # XPath for the name search input in Admin > User Management
    NAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input"
    
    # XPath for the user row in table with username 'samzo'
    CHECK_USER_INPUT = "//div[normalize-space()='samzo']"
    
    # XPath for the Assign Leave button in Leave menu
    ASSIGN_LEAVE = "//a[contains(text(), 'Assign Leave')]"
    
    # XPath for the Assign Claim button in Claim menu
    ASSIGN_CLAIM = "//button[normalize-space()='Assign Claim']"
    
    # XPath for the Event Type dropdown in Claim form
    EVENT_TYPE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]"
    
    # XPath for the Currency Type dropdown in Claim form
    CURRENCY_TYPE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]"
    
    # XPath for Indian currency selection from dropdown
    INDIAN_CURRENCY = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]"
    
    # XPath for the Create button in Claim form
    CLAIM_CREATE_BUTTON = "//button[normalize-space()='Create']"
    
    # XPath for the Leave Type dropdown in Assign Leave form
    LEAVE_TYPE = "//div[@class='oxd-select-text-input']"
    
    # XPath for From Date input field in Assign Leave form
    FROM_DATE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/input"
    
    # XPath for Till Date input field in Assign Leave form
    TILL_DATE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input"
    
    # XPath for the confirmation pop-up "Ok" button
    POP_UP = "//button[normalize-space()='Ok']"

    # XPath for the Personal Details link in My Info section
    PERSONAL_DETAILS = "//a[text()='Personal Details']"
    
    # XPath for the Contact Details link in My Info section
    CONTACT_DETAILS = "//a[text()='Contact Details']"
    
    # XPath for the Emergency Contacts link in My Info section
    EMERGENCY_CONTACTS = "//a[text()='Emergency Contacts']"
