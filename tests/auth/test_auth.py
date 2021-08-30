import pytest
from selenium.common.exceptions import TimeoutException

from common.constants import LoginConstants
from models.auth import AuthData


class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData(login="admin", password="Vjcrdf2!")
        app.login.auth(data)
        assert app.login.is_auth(), "We are not auth"

    def test_auth_invalid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps
        1. Open auth page
        2. Auth with empty data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    def test_auth_empty_login_and_password(self, app):
        """
        Steps
        1. Open main page
        2. Auth with empty data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, "login", None)
        setattr(data, "password", None)
        app.login.auth(data)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    def test_auth_login_as_guest(self, app):
        """
        Steps
        1. Open auth page
        2. If we are authenticated do logout
        3. Click on login as a guest button
        4. Check we are at the main page
        """
        app.open_auth_page()

        login_form = app.login.find_login_form()

        if not login_form:
            app.login.click_element(app.login.confirm_exit())

        app.login.click_element(app.login.login_as_guest_button())

        login_button = app.login.find_login_button()

        assert login_button is not None, "logging as guest don't work"
