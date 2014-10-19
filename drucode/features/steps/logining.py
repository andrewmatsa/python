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
    @given('opening browser with home page')
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
    @when('all link are works and present texts')
    def test_links(self):
        driver = self.driver

#         body = self.driver.find_element_by_css_selector('body')
#         self.assertIn('We are worldwide service providers.', body.text)
#
        self.driver.find_element_by_link_text("Approach").click()
        # body = self.driver.find_element_by_css_selector('body')
        # f = self.assertIn('Scrum methodology is a part of Agile development framework', body.text)
#
        self.driver.find_element_by_link_text("Clients").click()
#         body = self.driver.find_element_by_css_selector('body')
#         self.assertIn('Energy of this team never goes out.', body.text)
#
        self.driver.find_element_by_link_text("Philosophy").click()
#         body = self.driver.find_element_by_css_selector('body')
#         self.assertIn('We believe that', body.text)
#
        self.driver.find_element_by_link_text("Contact").click()
#         body = self.driver.find_element_by_css_selector('body')
#         self.assertIn('Choose your budget:', body.text)

        self.driver.find_element_by_link_text("Blog").click()
        # body = self.driver.find_element_by_css_selector('body')
        # self.assertIn('Our thoughts on technology, life, wisdom.', body.text)




class Test_links(Test1):
    @when('all link are works and present texts')

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
          body_text = find_body(search_text)

        driver = self.driver







    @step('comeback to the home page')
    def comeback_to_the_home(self):
        self.driver.find_element_by_xpath("html/body/header/div/div[1]/a/img").click()


class Test_Tell_Us_popup(Test1):
    @then('open the "Tell us" pop up')
    def test_form(self):
        driver = self.driver
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # open "Tell us about you project"
        self.driver.find_element_by_xpath(".//*[@id='section-preface-second']/div/div/div/div[1]/span[2]/a[1]")\
            .click()
        self.driver.implicitly_wait(5)
    # 50k
        self.driver.find_element_by_xpath(".//*[@id='contact-site-form']/div/div[2]/div[2]/div").click()
    # 150k+
        self.driver.find_element_by_xpath(".//*[@id='contact-site-form']/div/div[2]/div[3]/div").click()
    # 15k
        self.driver.find_element_by_xpath(".//*[@id='contact-site-form']/div/div[2]/div[1]/div").click()

    @step('fill all fields click button send')
    def fill_all_fields(self):
        driver = self.driver
        your_name = self.driver.find_element_by_xpath(".//*[@id='edit-name']").send_keys("Client name")
        your_email = self.driver.find_element_by_xpath(".//*[@id='edit-mail']").send_keys("test.andrew@mail.com")
        message = self.driver.find_element_by_xpath(".//*[@id='edit-message']").send_keys("Hello, I would like to "
                                                                                          "buy your company! And I have "
                                                                                          "a lot of question")
        button_submit = self.driver.find_element_by_xpath(".//*[@id='edit-submit']").click()
        # self.driver.find_element_by_xpath(".//*[@id='contact-form-wrapper']/div/div/div/a").click()

# class Test_contact_form(Test1):
#     def is_text_present(self, text):
#         try:
#             body = self.driver.find_element_by_tag_name("body") # find body tag element
#         except NoSuchElementException, e:
#             return False
#         return text in body.text # check if the text is in body's text


class Test_Incoming_Message_to_admin(Test1):
    @given('login as admin')
    def test_login_as_admin(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://admin:dr@develop.dr.web.drucode.com/login")
        user = self.driver.find_element_by_id('edit-name').send_keys('Developer')
        passw = self.driver.find_element_by_id('edit-pass').send_keys('admin_developer')
        button_submit = self.driver.find_element_by_id('edit-submit').click()

    @step('go to the drucode settings')
    def open_settings(self):
        driver = self.driver
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//*[@id='admin-menu-menu']/li[7]/a").click()
        self.driver.find_element_by_xpath("//*[@id='admin-menu-menu']/li[7]/ul/li[4]/a").click()

    @when('you are on contact message tab')
    def page_opened(self):
        self.driver.find_element_by_xpath(".//*[@id='branding']/ul/li[3]/a").click()

    @then('find the user,mail,budget,message')
    def cheking_the_same_data(self):
        self.driver.implicitly_wait(100)
        # assert "Test Name" in self.driver.get_page_source()
        # assert(self.driver.PageSource.Contains('Test Name'))
        # assert(selenium.isTextPresent("Test Name")
        #
        # Assert.IsTrue(driver.PageSource.Contains("rer"));

# http://assertselenium.com/2012/10/30/transformation-from-manual-tester-to-a-selenium-webdriver-automation-specialist/
# http://selenium2.ru/docs/test-design-considerations.html

    @step('all steps are passed')
    def tearDown(self):
        self.driver.close()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

