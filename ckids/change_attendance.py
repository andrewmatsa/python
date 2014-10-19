from selenium import webdriver
from pageobjects.base.basepageelement import BasePageElement
from pageobjects import locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from applitools.eyes import Eyes

class SignupTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://admin:ckids@develop.ckids.web.drucode.com")


class UsernameElement(BasePageElement):
    def __init__(self):
        self.locator = locators["login.username"]

    def __set__(self, obj, val):
       driver = webdriver.driver
       driver.find_element_by_id(self.locator).send_keys(val)


class PasswordElement(BasePageElement):
  def __init__(self):
    self.locator = locators["login.password"]

  def __set__(self, instance, value):
    driver = webdriver.driver
    driver.find_element_by_id(self.locator).send_keys(value)

        # driver.find_element_by_id("edit-name").send_keys("admin")
        # driver.find_element_by_id("edit-pass").send_keys("admin")

class LoginPageObject(BasePageObject):
  username = UsernameElement()
  password = PasswordElement()

  def __init__(self, driver, base_url):
    self.driver = driver
    self.driver.get(base_url)
    driver.find_element_by_id(locators["login.open"]).click()
    self.wait_for_element_displayed_by_id(self.driver, "id_username")
    self.assertEqual("Login", self.driver.title)
  def submit(self):
    self.driver.find_element_by_id(locators["login.submit"]).click()
    self.wait_for_page_title(self.driver, "Profile", msg="[error]: we are not logged in")





#
#
#     # Actions
#     def submit(self):
#         self.driver.find_element_by_id("edit-submit").click()
#
#     def cancel(self):
#         self.driver.find_element_by_class_name("cancel-button").click()
#
#     def backbutton(self):
#         self.driver.find_element_by_class_name("back-button").click()
#
#     def wait(self):
#         self.driver.implicitly_wait(30)
#
#
#
# class Attandance(unittest.TestCase):
#     def testattandance(self):
#         self.driver = webdriver.Firefox()
#         self.driver.find_element_by_link_text("Centres").click()
#         self.driver.find_element_by_xpath("html/body/div[1]/div/section/div[2]/div[2]/table/tbody/tr[2]/td[6]/a").click()
#         dropdownoption = self.driver.find_element_by_id("edit-field-centre-attendance-und")
#         self.driver.find_element_by_link_text("Centres").click()
#         self.driver.find_element_by_xpath("html/body/div[1]/div/section/div[2]/div[2]/table/tbody/tr[2]/td[6]/a").click()
#
#         dropdownoption = self.driver.find_element_by_id("edit-field-centre-attendance-und")
#         flag = False
#         for option in dropdownoption.find_elements_by_tag_name('option'):
#             if option.text == 'Carer managed attendance':
#             # if option.text == 'Front desk drop off / pick up':
#                 option.click()
#                 print ('You selected: ' + option.text)
#                 flag = True
#         if (flag != True):
#             print ("Error. Can't find option")
#         self.driver.implicitly_wait(30)


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
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
