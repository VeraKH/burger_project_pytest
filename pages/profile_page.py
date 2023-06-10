from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    # метод получения значения поля Имя
    def get_name_in_profile(self):
        return self.driver.find_element(*ProfilePageLocators.NAME).get_attribute('value')

    # метод получения значения поля Email
    def get_email_in_profile(self):
        return self.driver.find_element(*ProfilePageLocators.EMAIL).get_attribute('value')

    def click_log_out_button(self):
        self.driver.find_element(*ProfilePageLocators.LOG_OUT).click()

    def get_all_values_in_profile_fields(self):
        field_values_dic = {
            'name': self.get_name_in_profile(),
            'email': self.get_email_in_profile(),
        }
        field_values_list = list(field_values_dic.values())
        return field_values_list
