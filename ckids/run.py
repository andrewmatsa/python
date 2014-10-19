class Page(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self,
                 selenium_driver,
                 base_url='http://admin:ckids@develop.ckids.web.drucode.com',
                 short_url='http://develop.ckids.web.drucode.com'):
        self.base_url = base_url
        self.short_url = short_url
        self.driver = selenium_driver
        # self.timeout = 30

    def _open(self, url):
        auth_url = self.base_url
        self.driver.get(auth_url)

        short_url = self.short_url + url
        self.driver.get(short_url)

        assert self.on_page(), 'Did not land on %s' % url
 
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
 
    def open(self):
        self._open(self.url)
 
    def on_page(self):
        return self.driver.current_url == (self.short_url + self.url)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print '%s page does not have "%s" locator' % (self, loc)
 
 
# class LoginPage(Page):
#     """
#     Model the login page.
#     """
#     url = '/user'
#
#     # Locators
#     _loginuser = (By.ID, 'edit-name')
#     _password_loc = (By.ID, 'edit-pass')
#     _submit_loc = (By.ID, 'edit-submit')
#
#     # Actions
#     def open(self):
#         self._open(self.url)
#
#     def type_login(self, login):
#         self.find_element(*self._loginuser).send_keys(login)
#
#     def type_password(self, password):
#         self.find_element(*self._password_loc).send_keys(password)
#
#     def submit(self):
#         self.find_element(*self._submit_loc).click()
#
#
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
#         # Selenium
#         driver = webdriver.Firefox()
#         username = 'admin'
#         password = 'admin'
#         test_that_user_can_login(driver, username, password)
#     finally:
#         # Close the browser window
#         driver.close()
#
# if __name__ == '__main__':
#     main()
