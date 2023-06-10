import time
from pages.profile_page import ProfilePage
from locators.profile_page_locators import ProfilePageLocators


class TestProfilePage:

    def test_after_log_out_can_goes_to_login_page(self, driver, login):
        # goes to profile page
        profile_page = ProfilePage(driver, 'https://stellarburgers.nomoreparties.site/account')
        profile_page.open()
        # wait for page to load
        profile_page.wait_element_is_visible(ProfilePageLocators.SAVE)
        profile_page.click_log_out_button()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_values_in_profile_fields_and_user_data(self, driver, login, login_data):
        # goes to profile page
        profile_page = ProfilePage(driver, 'https://stellarburgers.nomoreparties.site/account')
        profile_page.open()
        # wait for page to load
        profile_page.wait_element_is_visible(ProfilePageLocators.SAVE)
        # make list of user's login data
        selected_values_list = [login_data['name'], login_data['email']]
        # get values from inputs
        values_from_field = profile_page.get_all_values_in_profile_fields()
        assert selected_values_list == values_from_field






