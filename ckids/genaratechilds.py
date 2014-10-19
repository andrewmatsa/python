from faker import Faker
import os
fake = Faker()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

        # chromedriver = "c:/chromedriver"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # self.driver = webdriver.Chrome(chromedriver)

        # IEDriverServer = "c:/IEDriverServer"
        # os.environ["webdriver.ie.driver"] = IEDriverServer
        # self.driver = webdriver.Ie(IEDriverServer)


# ----------------------------------------------------------------------------------------------------------

    def test_login(self):
        self.driver.get("http://admin:ckids@develop.ckids.web.drucode.com")
        driver = self.driver
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("andy_sniper")
        driver.find_element_by_id("edit-pass").send_keys("andy_sniper")
        driver.find_element_by_id("edit-submit").click()
        self.driver.implicitly_wait(30)
#ADD child
        for i in range(0,400):
            driver.find_element_by_link_text("Children").click()
            driver.find_element_by_xpath("html/body/div[1]/div/section/div/div[1]/a").click()
            # first name
            driver.find_element_by_xpath(".//*[@id='edit-title']").send_keys(fake.name().split()[0])
            # last name
            driver.find_element_by_xpath(".//*[@id='edit-field-child-second-name-und-0-value']")\
                .send_keys(fake.name().split()[1])


            dropdownoption = driver.find_element_by_id("edit-field-child-room-und")
            flag = False
            for option in dropdownoption.find_elements_by_tag_name('option'):
                # if option.text == 'Carer managed attendance':
                if option.text == 'room 2':
                    option.click()
                    flag = True
            driver.find_element_by_id("edit-submit").click()
            driver.get("http://develop.ckids.web.drucode.com")


# ----------------------------------------------------------------------------------------------------
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
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
