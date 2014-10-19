from selenium import webdriver
from behave import when, then, then
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox() # Get local session of firefox
browser.get("http://www.yahoo.com") # Load page
elem = browser.find_element_by_name("p") # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
browser.find_element_by_link_text("SeleniumHQ - Selenium - Web Browser Automation")

browser.close()
