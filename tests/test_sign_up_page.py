import os
import allure
import re
from generator.generator import generated_person, generate_file
from pages.sign_up_page import SignUpPage


class TestSignUpPageValues:
    person = generated_person()
    path = generate_file()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('open browser, goes to sign up page, fill all the inputs and check check email field value is not empty, close the browser')  # декораторы
    @allure.title('check email field value is not empty after user filled the form')
    def test_email_field_not_empty(self, driver):
        sign_up_page = SignUpPage(driver, 'https://stellarburgers.nomoreparties.site/register')
        sign_up_page.open()
        sign_up_page.sign_up_input(self.person.name, self.person.email, self.person.password)
        # get name field value and check that it's not empty
        email_value = sign_up_page.get_email_in_field()
        assert len(email_value) > 0

    @allure.severity(allure.severity_level.MINOR)
    @allure.description('open browser, goes to sign up page, fill all the inputs and check check email fits the patern value is not empty, close the browser')
    @allure.title('check email value fits the pattern of email')
    def test_email_field_fits_the_pattern(self, driver):
        sign_up_page = SignUpPage(driver, 'https://stellarburgers.nomoreparties.site/register')
        sign_up_page.open()
        sign_up_page.sign_up_input(self.person.name, self.person.email, self.person.password)
        email_value = sign_up_page.get_email_in_field()
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        assert re.match(pattern, email_value)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('open browser, goes to sign up page, fill all the inputs and check check password os more than 6 symbols')
    @allure.title('check password value is more than 6 symbols')
    def test_len_pass_more_than_6(self, driver):
        sign_up_page = SignUpPage(driver, 'https://stellarburgers.nomoreparties.site/register')
        sign_up_page.open()
        sign_up_page.sign_up(self.person.name, self.person.email, self.person.password)
        # get password field value and check that it is 6 or more symbols
        pass_value = sign_up_page.get_password_in_field()
        assert len(pass_value) >= 6

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('open browser, goes to sign up page, fill all the inputs and incorrect password and check the error message')
    @allure.title('check that error message appears if password value is less than 6 symbols')
    def test_pass_error_message_appears(self, driver):
        sign_up_page = SignUpPage(driver, 'https://stellarburgers.nomoreparties.site/register')
        sign_up_page.open()
        sign_up_page.sign_up(self.person.name, self.person.email, self.person.incorrect_password)
        pass_error_value = sign_up_page.get_error_massage_in_pass_field()
        assert pass_error_value == 'Некорректный пароль'

    os.remove(path)
