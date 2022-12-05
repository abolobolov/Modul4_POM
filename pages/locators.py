from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link')
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-default')


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_NULL = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators:
    BUTTON_OPEN_FORM = (By.CSS_SELECTOR, '#registration_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_BOOK = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    MESSAGES_VIN = (By.CSS_SELECTOR, '#messages > div:nth-child(1)>div>strong')
    PRICE_BOOK = (By.CSS_SELECTOR, 'div.col-sm-6.product_main>p.price_color')
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")
