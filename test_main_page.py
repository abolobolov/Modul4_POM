from selenium.webdriver.common.by import By

from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"



def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")  # registration_link
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_visible_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
