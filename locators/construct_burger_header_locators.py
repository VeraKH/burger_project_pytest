from selenium.webdriver.common.by import By


class HeaderPageLocators:

    # buttons
    CONSTRUCTOR = [By.XPATH, '//p[contains(text(), "Конструктор")]']
    ORDERS = [By.XPATH, '//p[contains(text(), "Лента Заказов")]']
    HOME = [By.XPATH, './/a[@href="/"]']
    PROFILE = [By.XPATH, '//p[contains(text(), "Личный Кабинет")]']

