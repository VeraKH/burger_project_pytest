from selenium.webdriver.common.by import By


class BurgerBasketPageLocators:

    # buttons
    LOG_IN = [By.XPATH, './/button[contains(text(), "Войти в аккаунт")]']
    MAKE_ORDER = [By.XPATH, './/button[contains(text(), "Оформить заказ")]']
    LOG_IN_OR_MAKE_ORDER = [By.XPATH, './/button[contains(@class,"33qZ0 button_button")]']
    CONSTRUCT_ELEMENT_BASKET = [By.XPATH, './/span[contains(text(), "Перетяните булочку сюда")]']
