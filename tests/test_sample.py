from pages.gmail_login import GmailLogin
import time


def test_login(driver, config):
    email = config['APPLICATION']['username']
    password = config['APPLICATION']['password']
    gmail_login = GmailLogin(config, driver)
    gmail_login.navigate()
    gmail_login.sign_in(email, password)
    time.sleep(10)
