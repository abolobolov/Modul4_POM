class BasketPage:
    def should_null_basket(self):
        basket_null = self.browser.find_element(*BasketPageLocators.BASKET_NULL)
        print(basket_null.text)
        assert basket_null.text, 'Корзина не пуста'
