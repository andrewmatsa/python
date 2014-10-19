from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os
import urlparse
from applitools.eyes import Eyes

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        Eyes.api_key = '8PN69qEtrGKMMYrzyThC8wWXLlFmqyPMH1YLurYcxp8110'
        eyes = Eyes()
        self.driver = eyes.open(driver=self.driver, app_name='Applitools', test_name='Test Web Page',
                       viewport_size={'width': 1024, 'height': 768})


    def test_login(self):
        self.driver = self.eyes.open(driver=self.driver, app_name='Applitools', test_name='Test Web Page',
                       viewport_size={'width': 1024, 'height': 768})
        self.eyes.check_window('Main Page')
        self.driver.get("http://develop.stamps_ru.web.drucode.com/ru")
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
