class TestLogIn:

    # Check that after login opens main page
    def test_login_move_to_main_page(self, driver, login):
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

