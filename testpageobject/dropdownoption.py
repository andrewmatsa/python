from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from applitools.eyes import Eyes

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()


        dropdownoption = self.find_element_by_id("edit-field-centre-attendance-und")
        flag = False
        for option in dropdownoption.find_elements_by_tag_name('option'):
            if option.text == 'Carer managed attendance':
            # if option.text == 'Front desk drop off / pick up':
                option.click()
                print ('You selected: ' + option.text)
                flag = True
        if (flag != True):
            print ("Error. Can't find option")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("edit-submit").click()

#

    # def tearDown(self):
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
