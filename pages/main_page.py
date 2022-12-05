from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .base_page import BasePage
from .locators import MainPageLocators, BasePageLocators, BasketPageLocators


class MainPage(BasePage):
    # def __init__(self, *args, **kwargs):
    #   super(MainPage, self).__init__(*args, **kwargs)
    def perehod_v_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BUTTON_TO_BASKET)
        basket.click()

    def should_null_basket(self):
        basket_null = self.browser.find_element(*BasketPageLocators.BASKET_NULL)
        print(basket_null.text)
        assert basket_null.text, 'Корзина не пуста'
