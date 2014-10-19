class BasePage(object):
  url = None

  def __init__(self, driver):
      self.driver = driver

  def fill_form_by_css(self, form_css, value):
      elem = self.driver.find(form_css)
      elem.send_keys(value)

  def fill_form_by_id(self, form_element_id, value):
      return self.fill_form_by_css('#%s' % form_element_id, value)

  def navigate(self):
      self.driver.get(self.url)


class Homepage(BasePage):
  url = "http://localhost:8000"

  def getSignupForm(self):
      return SignupPage(self.driver)

class SignupPage(BasePage):
  url = "http://localhost:8000/account/create/"

  def setName(self, first, last):
      self.fill_form_by_id("id_first_name", first)
      self.fill_form_by_id("id_last_name", last)

  def setEmail(self, email):
      self.fill_form_by_id("id_email", email)

  def setPassword(self, password):
      self.fill_form_by_id("id_password", password)
      self.fill_form_by_id("id_password_confirmation", password)

  def setProductName(self, name):
      self.fill_form_by_id("id_first_product_name", name)

  def submit(self):
      self.driver.find('#create_account_form button').click()
      return OnboardingInvitePage(self.driver)