from typing import Optional

from selenium.webdriver.remote.webelement import WebElement

from models.auth import AuthData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SUBMIT)

    def login_as_guest_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN_AS_GUEST_BUTTON)

    def find_login_button(self) -> Optional[WebElement]:
        try:
            return self.find_elements(LoginPageLocators.LOGIN_BUTTON)[0]
        except IndexError:
            return

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def confirm_exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.CONFIRM_EXIT)

    def find_login_form(self) -> Optional[WebElement]:
        try:
            return self.find_elements(LoginPageLocators.LOGIN_FORM)[0]
        except IndexError:
            return

    def auth(self, data: AuthData):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def auth_login_error(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text
