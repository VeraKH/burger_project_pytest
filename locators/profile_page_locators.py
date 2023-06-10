from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # inputs
    NAME = [By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input"]
    EMAIL = [By.XPATH, ".//label[contains(text(), 'Логин')]/following-sibling::input"]

    # buttons
    SAVE = [By.XPATH, './/button[contains(text(), "Сохранить")]']
    LOG_OUT = [By.XPATH, './/button[contains(text(), "Выход")]']

