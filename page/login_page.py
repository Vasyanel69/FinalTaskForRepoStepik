from .base_page import BasePage
from conftest import browser
from page.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f'Неправильный {browser.current_url}'

        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_FORM), "Sign up form is not presented"

        assert True
