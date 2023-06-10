from locators.sign_up_page_locators import SignUpPageLocators
from pages.base_page import BasePage
import re
import allure


class SignUpPage(BasePage):

    @allure.step('Wait for sign up button')
    def wait_for_sign_up_button(self):
        self.wait_element_is_visible(SignUpPageLocators.SIGNUP)

    @allure.step('Set name to name field')
    def set_name(self, name):
        self.driver.find_element(*SignUpPageLocators.NAME).send_keys(name)

    @allure.step('Set name to email field')
    def set_email(self, password):
        self.driver.find_element(*SignUpPageLocators.EMAIL).send_keys(password)

    # метод заполняет поле «Password»
    @allure.step('Set password to password field')
    def set_password(self, password):
        self.driver.find_element(*SignUpPageLocators.PASSWORD).send_keys(password)

    @allure.step('Click sign up button')
    def click_sign_up_button(self):
        self.driver.find_element(*SignUpPageLocators.SIGNUP).click()

    @allure.step('Click log in button')
    def click_log_in_button(self):
        self.driver.find_element(SignUpPageLocators.SIGNIN)

    def sign_up_input(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)

    def sign_up(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_sign_up_button()

        # метод получения значения поля Имя
    @allure.step('Get name from name field')
    def get_name_in_field(self):
        return self.driver.find_element(*SignUpPageLocators.NAME).get_attribute('value')

        # метод получения значения поля Email
    @allure.step('Get email from email field')
    def get_email_in_field(self):
        return self.driver.find_element(*SignUpPageLocators.EMAIL).get_attribute('value')

    @allure.step('Get password from password field')
    def get_password_in_field(self):
        return self.driver.find_element(*SignUpPageLocators.PASSWORD).get_attribute('value')

    @allure.step('Get error massege under password field')
    def get_error_massage_in_pass_field(self):
        return self.driver.find_element(*SignUpPageLocators.PASS_ERROR).text

    @allure.step('Get True or false if email fits the pattern')
    def email_value_fits_the_pattern(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        email_returned = re.match(pattern, email)
        return email_returned
