from locators.burger_basket_page_locators import BurgerBasketPageLocators
from pages.base_page import BasePage


class BurgerBasketPage(BasePage):
    # get name of button Make Order
    def get_name_of_button_order(self):
        return self.driver.find_element(*BurgerBasketPageLocators.LOG_IN_OR_MAKE_ORDER).text

    # click on log in button
    def click_log_in_button(self):
        self.driver.find_element(*BurgerBasketPageLocators.LOG_IN).click()
