import pytest

from .pages.product_page import ProductPage

# link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.parametrize('link', ["okay_link",
#                                 pytest.param("bugged_link", marks=pytest.mark.xfail),
#                                "okay_link"])


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{link}/?promo=offer{no}" for no in range(10)]
link_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//?promo=offer0"


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.all_product_page()


@pytest.mark.message('link_2')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_2)
    page.open()
    page.button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.message('link_2')
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_2)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.message('link_2')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_2)
    page.open()
    page.button_add_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link3 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link3)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link4 = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-big-u_93/"
    page = ProductPage(browser, link4)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link5 = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page =