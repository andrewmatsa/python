from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from behave import given, when, then, step
import os
import urlparse
from splinter import Browser

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    # def setUp(self):
        # if (self.driver == 'Chrome'):
        #     self.driver = webdriver.Chrome()
        # else:
        #     self.driver = webdriver.Firefox()

        # try:
        #     chromedriver = "c:/chromedriver"
        #     os.environ["webdriver.chrome.driver"] = chromedriver
        #     self.driver = webdriver.Chrome(chromedriver)
        # except:
        #     self.driver = webdriver.Firefox()
        #


        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--proxy-server=%s')
        # driver = webdriver.Chrome(
        #     executable_path=r"c:\chromedriver.exe",
        #     chrome_options=chrome_options)

        # browser = Browser('chrome')


        # IEDriverServer = "c:/IEDriverServer"
        # os.environ["webdriver.ie.driver"] = IEDriverServer
        # self.driver = webdriver.Ie(IEDriverServer)

 # ----------------------------------------------------------------------------------------------------------

    def test_login(self):
        self.driver.get("http://develop.dtu.learn.mentorix.dk/user/")
        driver = self.driver
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("admin")
        driver.find_element_by_id("edit-pass").clear()
        driver.find_element_by_id("edit-pass").send_keys("admin")
        driver.find_element_by_id("edit-submit").click()
        self.driver.implicitly_wait(30)
        self.driver.get("develop.dtu.learn.mentorix.dk/module/9837")
        self.driver.set_window_size(1400,800)
        driver.find_element_by_id("edit-trigger-link").click()
        driver.find_element_by_xpath(".//*[@id='panels-ipe-paneid-new-"
                                     "51']/div[2]/div/div/div/div[2]/div/div").click()
        # click on "Image collection icon"
        driver.find_element_by_xpath(".//*[@id='cke_29']/span[1]").click()
        element = driver.find_element_by_class_name("cke_dialog_ui_button")
        print element.location['x']
        print element.location['y']
        # print element.size()
        # print element.is_displayed()
        # location = e.location
        # size = e.size
        # print(location)
        # print(size)



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
