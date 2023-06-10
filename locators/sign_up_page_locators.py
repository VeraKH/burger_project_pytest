from selenium.webdriver.common.by import By


class SignUpPageLocators:
    # inputs
    NAME = [By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input"]
    EMAIL = [By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input"]
    PASSWORD = [By.XPATH, ".//label[contains(text(), 'Пароль')]/following-sibling::input"]

    # buttons
    SIGNUP = [By.XPATH, './/button[contains(text(), "Зарегистрироваться")]']
    SIGNIN = [By.XPATH, './/a[contains(text(), "Войти")]']

    # error
    PASS_ERROR = [By.CLASS_NAME, 'input__error']
