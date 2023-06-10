from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import re
from locators.construct_burger_page_locators import ConstructBurgerPageLocators
from pages.base_page import BasePage


class ConstructBurger(BasePage):

    def get_class_of_selected_buns_elements(self):
        return self.driver.find_element(*ConstructBurgerPageLocators.BUN).get_attribute('class')

    def get_class_of_selected_souses_elements(self):
        return self.driver.find_element(*ConstructBurgerPageLocators.SOUSES).get_attribute('class')

    def get_class_of_selected_filling_elements(self):
        return self.driver.find_element(*ConstructBurgerPageLocators.FILLING).get_attribute('class')

    def click_bun_button(self):
        self.driver.find_element(*ConstructBurgerPageLocators.BUN).click()

    def click_souses_button(self):
        self.driver.find_element(*ConstructBurgerPageLocators.SOUSES).click()

    def click_filling_button(self):
        self.driver.find_element(*ConstructBurgerPageLocators.FILLING).click()

