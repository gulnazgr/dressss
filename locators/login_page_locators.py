from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#page-site-index .usermenu .login")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    LOGIN_AS_GUEST_BUTTON = (By.CSS_SELECTOR, "form#guestlogin > button[type=submit]")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    CONFIRM_EXIT = (By.CSS_SELECTOR, "form[method=post][action*=logout] button[type=submit]")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
