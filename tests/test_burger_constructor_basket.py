import time

from pages.burger_basket_page import BurgerBasketPage
from locators.burger_basket_page_locators import BurgerBasketPageLocators


class TestBurgerConstructorBasket:

    def test_login_btn_is_for_guest(self, driver):
        burger_basket_page = BurgerBasketPage(driver, 'https://stellarburgers.nomoreparties.site/')
        burger_basket_page.open()
        burger_basket_page.wait_element_is_visible(BurgerBasketPageLocators.CONSTRUCT_ELEMENT_BASKET)
        assert burger_basket_page.get_name_of_button_order() == 'Войти в аккаунт'

    def test_make_order_button_after_login(self, driver, login, login_data):
        burger_basket_page = BurgerBasketPage(driver, 'https://stellarburgers.nomoreparties.site/')
        burger_basket_page.open()
        burger_basket_page.wait_element_is_visible(BurgerBasketPageLocators.MAKE_ORDER)
        assert burger_basket_page.get_name_of_button_order() == 'Оформить заказ'
