class BasePage(object):
    url = None
    def __init__(self, driver):
        self.driver = driver

    # def fill_form_by_css(self, form_css, input):
    #     elem = self.driver.find(form_css)
    #     elem.send_keys(input)
    #
    # def fill_form_by_id(self, form_element_id, input):
    #     return self.fill_form_by_css('#%s' % form_element_id, input)
    #
    #   # added
    # def fill_form_by_xpath(self, form_element_xpath, input):
    #     return self.fill_form_by_xpath('#%s' %  form_element_xpath, input)

    def navigate(self):
        self.driver.get(self.url)

  
class Homepage(BasePage):
    url = "http://jobsuma.qa.s1.drucode.com"

    def getRegistration(self):
        self.driver.set_window_size(1920,1024)
        self.driver.find_element_by_xpath("html/body/div[1]/div/ul/li[3]/div/a").click()
        return SignupPage(self.driver)
  
class SignupPage(BasePage):
    url = "http://jobsuma.qa.s1.drucode.com"

    def setName(self):
        self.driver.find_element_by_id("edit-company-name")

    # def set_employees(self, name):
    #     self.driver.find_element_by_id("edit-vat-number", name)
