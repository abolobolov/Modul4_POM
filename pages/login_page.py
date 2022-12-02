from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.click_to_button_Login_Or_Register()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def click_to_button_Login_Or_Register(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Не корректный url адрес'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
