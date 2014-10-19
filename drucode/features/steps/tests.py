from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest
from behave import given, when, then,step
from selenium.webdriver.common.keys import Keys
from selenium import selenium
import csv
import random
from selenium.webdriver.support.ui import WebDriverWait
import thread


class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://admin:dr@develop.dr.web.drucode.com")
        # chrome_options = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome(
        #     executable_path=r"c:\chromedriver.exe",
        #     chrome_options=chrome_options)

    def tearDown(self):
        self.driver.close()

class Test_links(Test1):
    def test_links(self):
        driver = self.driver

class Test_links(Test1):
    def find_body(self, search_text):
      body = self.driver.find_element_by_css_selector('body')
      body_response = self.assertIn(search_text, body.text)
      return body_response

    def test_links(self):

        queue = [
          ("Approach", "Scrum methodology is a part of Agile development framework"),
          ("Clients", "Energy of this team never goes out."),
          ("Philosophy", "We believe that"),
          ("Contact", "Choose your budget:"),
          ("Blog", "Our thoughts on technology, life, wisdom."),
        ]

        for text, search_text in queue:
          self.driver.find_element_by_link_text(text).click()
          self.find_body(search_text)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

