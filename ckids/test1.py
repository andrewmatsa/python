from selenium import webdriver
from aqa.python.ckids.pages.login import LoginPage

def test_that_user_can_login(driver, username, password):
    """
    Test that the user identified by the given credentials can login
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.type_login(username)
    login_page.type_password(password)
    login_page.submit()

    # Make sure we got past the login page
    assert not login_page.on_page(), "Couldn't get past the login page"

def main():
    try:
        # Selenium
        driver = webdriver.Firefox()
        username = 'admin'
        password = 'admin'
        test_that_user_can_login(driver, username, password)
    finally:
        # Close the browser window
        driver.close()

if __name__ == '__main__':
    main()
