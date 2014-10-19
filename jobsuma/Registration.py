from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re
from jobsuma.Base import Homepage


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.browser= webdriver.Firefox()

    def test_registration(self):
        self.browser.get("http://jobsuma.qa.s1.drucode.com")
        self.browser.find_element_by_xpath("html/body/div[1]/div/ul/li[3]/div/a").click()
        self.browser.implicitly_wait(30)

        company_name = self.browser.find_element_by_id("edit-company-name")
        company_name.send_keys("test")

        num_of_employee = self.browser.find_element_by_id("edit-no-employees")
        num_of_employee.send_keys("33")

        company_site = self.browser.find_element_by_id("edit-site")
        company_site.send_keys('http://drucode.com')

        vat_numb = self.browser.find_element_by_id("edit-vat-number")
        vat_numb.send_keys("123")

        street_name = self.browser.find_element_by_id("")

        plz = self.browser.find_element_by_id("")

        number = self.browser.find_element_by_id("")

        location = self.browser.find_element_by_id("")

        land_dropdown =

        logo_upload = edit-logo-path-upload

        Salutation

        titel

        name = edit-contact-firstname

        surname = edit-contact-name

        phone_number = edit-contact-telephone

        fax = edit-contact-fax

        department = edit-contact-department

        email = edit-email-address

        billing_address_checkbox = .//*[@id='edit-billing']/div/div[1]/label/span





        # driver.set_window_size(1920,1024)
        # driver.find_element_by_xpath("html/body/div[1]/div/ul/li[3]/div/a").click()





    # def testsetCompanyName(self, name):
    #     self.driver.find_element_by_id("edit-company-name",name)

    # def registration(self):
    #     driver = self.driver
    #     driver.find_element_by_id("edit-title").clear()
    #     driver.find_element_by_id("edit-title").send_keys("test article 4")
    #     # driver.find_element_by_id("edit-field-tags-und").clear()
    #     driver.find_element_by_id("edit-field-tags-und").send_keys("tag3")
    #     expected = driver.find_element_by_xpath(".//*[@id='edit-body-und-0-value']").send_keys("Lorem")
    #     driver.find_element_by_id("edit-body-und-0-format--2").send_keys()
    #     driver.find_element_by_id("edit-field-image-und-0-upload").send_keys("D:\\Photos\\Business man in suit.jpg")
    #     driver.find_element_by_id("edit-submit").click()
    #
    #     element = driver.find_element_by_class_name("field-item even").text
    #     if "Lorem" in element: print "I found my text"
        # ecpected text method

        # try:
        #     element = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        # finally:
        #     print element

    # def is_text_present(self, text):
    #     try: el = self.driver.find_element_by_tag_name("body")
    #     except NoSuchElementException, e: return False
    #     print text in el.text



    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True
    #
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException, e: return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True

    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)
    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
