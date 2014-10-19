from selenium import webdriver
import unittest
import time
from base import homepage

class SignupTest(unittest.TestCase):
  def setUp(self):
      self.browser = webdriver.Firefox()

  def test_someone_can_signup(self):
      homepage = Homepage(self.browser)
      homepage.navigate()
      signup_form = homepage.getSignupForm()
      signup_form.setName("Justin", "Abrahms")
      signup_form.setPassword("asdf")
      randomNumber = int(time.time())
      signup_form.setEmail('test+%s@example.com' % randomNumber)
      signup_form.setProductName('test')

      onboarding_1 = signup_form.submit()
      onboarding_2 = onboarding_1.next()
      onboarding_3 = onboarding_2.next()
      items_page = onboarding_3.next()

      elem = self.browser.find_element_by_css_selector('#logged_in_header')
      assert elem is not None

  def tearDown(self):
      self.browser.close()

if __name__ == "__main__":
  unittest.main()