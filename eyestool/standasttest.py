from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from applitools.eyes import Eyes


# This is your api key, make sure you use it in all your tests.
Eyes.api_key = '8PN69qEtrGKMMYrzyThC8wWXLlFmqyPMH1YLurYcxp8110' 
eyes = Eyes()

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
# Get a selenium web driver object.

def test_login(self):
    try:
        # Start visual testing with browser viewport set to 1024x768.
        # Make sure to use the returned driver from this point on.
        self.driver = eyes.open(driver=self.driver, app_name='Applitools', test_name='Test Web Page',
                           viewport_size={'width': 1024, 'height': 768})

        # Visual validation point #1
        eyes.check_window('main page what we have now')
        self.driver.get('http://admin:stamps_ru@develop.stamps_ru.web.drucode.com')

        eyes.check_window('next page')
        self.driver.get('http://admin:stamps_ru@develop.stamps_ru.web.drucode.com')
        # End visual testing. Validate visual correctness.
        self.driver.implicitly_wait(30)



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):

        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    # def tearDown(self):
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
