from selenium.webdriver.common.by import By


class ConstructBurgerPageLocators:

    # tabs
    BUN = [By.XPATH, './/span[contains(text(), "Булки>")]']
    SOUSES = [By.XPATH, './/span[contains(text(), "Соусы")']
    FILLING = [By.XPATH, './/span[contains(text(), "Начинки")']

    # elements
    flur_bun = [By.XPATH, './/p[contains(text(), "Флюоресцентная булка R2-D3")']
