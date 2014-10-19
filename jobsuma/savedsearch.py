from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://jobsuma.qa.s1.drucode.com")
        self.driver.implicitly_wait(30)
        self.base_url = "http://jobsuma.qa.s1.drucode.com"
        self.driver.get("http://jobsuma.qa.s1.drucode.com")
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        driver.find_element_by_id("edit-name").send_keys("admin")
        driver.find_element_by_id("edit-pass").send_keys("pass")
        driver.find_element_by_id("edit-submit").click()
        self.driver.implicitly_wait(30)

    def test_untitled(self):
        driver = self.driver
        driver.get("http://dehamd013.configcenter.info/alle-jobs")
        driver.find_element_by_id("field-job-title").click()
        # driver.find_element_by_id("field-job-title").clear()
        driver.find_element_by_id("field-job-title").send_keys("Developer")
        driver.find_element_by_id("edit-job-submit").click()
        driver.get("http://dehamd013.configcenter.info/node/add/saved-search")
    # el = driver.find_element_by_id("block-jobsuma-job-search")
    #         for option in el.find_elements_by_tag_name('input'):
    #             if option.text == 'create-saved-search last':
    #                 option.click() # select() in earlier versions of webdriver


        # driver.find_element_by_id("edit-title").clear()
        driver.find_element_by_id("edit-title").send_keys("Developer")
        driver.find_element_by_id("edit-field-jobart-und-0-value").send_keys("test")
        driver.find_element_by_id("edit-field-saved-search-category-und-0-value").send_keys("Jobs in")
        driver.find_element_by_id("edit-field-related-saved-searches-und-add-more").click()
        # driver.find_element_by_id("edit-field-h1-und-0-value").clear()
        driver.find_element_by_id("edit-field-h1-und-0-value").send_keys("test h1")
        driver.find_element_by_id("edit-submit").click()
        driver.find_elements_by_link_text("Alle").click()
        driver.find_elements_by_xpath("html/body/div[3]/div/section/ul/li[2]/a").click()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_text_present(self, text):
        try: el = self.driver.find_element_by_tag_name("body")
        except NoSuchElementException, e: return False
        return text in el.text

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

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
