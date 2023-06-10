from locators.construct_burger_header_locators import HeaderPageLocators
from pages.base_page import BasePage
import allure


class BurgerHeader(BasePage):

    # click on header buttons
    @allure.step('Click main "Constructor"button on the homepage')
    def click_constructor_button(self):
        self.driver.find_element(*HeaderPageLocators.CONSTRUCTOR).click()

    @allure.step('Click "Make order" button')
    def click_orders_button(self):
        self.driver.find_element(*HeaderPageLocators.ORDERS).click()

    @allure.step('Click Homepage button')
    def click_home_button(self):
        self.driver.find_element(*HeaderPageLocators.HOME).click()

    @allure.step('Click "Profile" button')
    def click_profile_button(self):
        self.driver.find_element(*HeaderPageLocators.PROFILE).click()
