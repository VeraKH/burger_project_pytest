from selenium.webdriver.common.by import By


class LoginPageLocators:

    # inputs
    EMAIL = [By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input"]
    PASSWORD = [By.XPATH, ".//label[contains(text(), 'Пароль')]/following-sibling::input"]

    # buttons
    LOGIN = [By.XPATH, './/button[contains(text(), "Войти")]']
    SIGN_UP = [By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]"]
