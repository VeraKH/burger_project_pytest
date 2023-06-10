from selenium import webdriver
import pytest
from pages.log_in_page import LogInPage
import allure


@allure.step('Open browser')
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login_data():
    return {
        'name': 'Nadya',
        'email': 'nadya_terekhina_5_123@yandex.ru',
        'password': '123456'
    }


@allure.step('Login system')
@pytest.fixture()
def login(driver, login_data):
    # log in system
    login_page = LogInPage(driver, 'https://stellarburgers.nomoreparties.site/login')
    login_page.open()
    login_page.log_in(login_data['email'], login_data['password'])
