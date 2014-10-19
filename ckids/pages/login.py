from selenium import webdriver
from selenium.webdriver.common.by import By
from aqa.python.ckids.run import Page

class LoginPage(Page):
    """
    Model the login page.
    """
    url = '/user'

    # Locators
    _loginuser = (By.ID, 'edit-name')
    _password_loc = (By.ID, 'edit-pass')
    _submit_loc = (By.ID, 'edit-submit')

    # Actions
    def open(self):
        self._open(self.url)

    def type_login(self, login):
        self.find_element(*self._loginuser).send_keys(login)

    def type_password(self, password):
        self.find_element(*self._password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self._submit_loc).click()


# def test_that_user_can_login(driver, username, password):
#     """
#     Test that the user identified by the given credentials can login
#     """
#     login_page = LoginPage(driver)
#
#     login_page.open()
#     login_page.type_login(username)
#     login_page.type_password(password)
#     login_page.submit()
#
#     # Make sure we got past the login page
#     assert not login_page.on_page(), "Couldn't get past the login page"
#
#
# def main():
#     try:
#         driver = webdriver.Firefox()
#         username = 'admin'
#         password = 'admin'
#         test_that_user_can_login(driver, username, password)
#     finally:
#         driver.close()
#
# if __name__ == '__main__':
#     main()