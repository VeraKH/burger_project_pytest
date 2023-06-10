import time
from locators.log_in_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LogInPage(BasePage):

    # waiting for page load
    def wait_for_load_page(self):
        self.wait_element_is_visible(LoginPageLocators.LOGIN)

    # метод заполняет поле «Email»
    def set_email(self, password):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(password)

    # метод заполняет поле «Password»
    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_log_in_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN).click()

    def log_in_input(self, email, password):
        self.set_email(email)
        self.set_password(password)

    def log_in(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_log_in_button()
        time.sleep(3)
