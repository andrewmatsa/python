from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

# ----------------------------------------------------------------------------------------------------------

    def test_login(self):
        self.driver.get("http://admin:ckids@develop.ckids.web.drucode.com")
        driver = self.driver
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("testandrew102_1")
        driver.find_element_by_id("edit-pass").clear()
        driver.find_element_by_id("edit-pass").send_keys("testandrew102_1")
        driver.find_element_by_id("edit-submit").click()
        self.driver.implicitly_wait(30)
#ADD + Nappy / Toilet
    def addnappy(self):
        self.find_element_by_link_text("+ Nappy / Toilet").click()
        self.find_element_by_xpath(".//*[@id='edit-nappy-details']/div[4]/label").click()
        self.find_element_by_xpath(".//*[@id='edit-n-ckids-children']/div/label").click()
        button_add = self.driver.find_element_by_id("edit-submit").click()

#ADD + Food
        driver.find_element_by_link_text("+ Food").click()
        dropdownfood = driver.find_element_by_id("edit-food-details")
        flag = False
        for option in dropdownfood.find_elements_by_tag_name('option'):
            if option.text == 'Banana':
                option.click()
                print ('You selected: ' + option.text)
                flag = True
        if (flag != True):
            print ("Error. Can't find option")
        driver.find_element_by_xpath(".//*[@id='edit-189-child-fieldset']/div/div[1]/label").click() # Dana  Rigurira
        driver.find_element_by_id("edit-submit--2").click()

#ADD + Sleep
        driver.find_element_by_link_text("+ Sleep").click()
        driver.find_element_by_xpath(".//*[@id='edit-sleep-details']/div[1]/label").click()  # Down to Sleep
        # driver.find_element_by_xpath(".//*[@id='edit-sleep-details']/div[2]/label").click()  # Up From Sleep
        # driver.find_element_by_xpath(".//*[@id='edit-sleep-details']/div[3]/label").click()  # Rest
        driver.find_element_by_xpath(".//*[@id='edit-s-ckids-children']/div/label").click()  # Dana  Rigurira
        driver.find_element_by_id("edit-submit--3").click()

#ADD + Activity
        driver.find_element_by_link_text("+ Activity").click()
        driver.find_element_by_id("edit-activity-details").send_keys("test Activity detail text")
        driver.find_element_by_xpath(".//*[@id='edit-a-ckids-children']/div/label").click()  # Dana  Rigurira
        driver.find_element_by_id("edit-submit--4").click()

#ADD + Photos
        driver.find_element_by_link_text("+ Photos").click()
        driver.find_element_by_id("edit-field-record-photo-title-und-0-value").send_keys("test photos")
        driver.find_element_by_id("edit-field-record-photo-und-0-upload").send_keys("D:\Photos\18.jpg")
        driver.find_element_by_xpath(".//*[@id='edit-field-record-photo-und-0-upload-button']").click()
        driver.find_element_by_xpath(".//*[@id='edit-field-record-child-und']/div/label").click() # Dana  Rigurira
        driver.find_element_by_id("edit-submit--5").click()


#ADD + Comments
        driver.find_element_by_link_text("+ Comments").click()
        driver.find_element_by_id("edit-comments-details").send_keys("today will be good day")
        driver.find_element_by_xpath(".//*[@id='edit-c-ckids-children']/div/label").click()  # Dana  Rigurira
        driver.find_element_by_id("edit-submit--6").click()




        # driver.find_element_by_xpath("html/body/div[1]/div/section/div[2]/div[2]/table/tbody/tr[2]/td[6]/a").click()
        # dropdownoption = driver.find_element_by_id("edit-field-centre-attendance-und")
        # flag = False
        # for option in dropdownoption.find_elements_by_tag_name('option'):
        #     if option.text == 'Carer managed attendance':
        #     # if option.text == 'Front desk drop off / pick up':
        #         option.click()
        #         print ('You selected: ' + option.text)
        #         flag = True
        # if (flag != True):
        #     print ("Error. Can't find option")
        # driver.find_element_by_id("edit-submit").click()


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
