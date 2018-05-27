import time


class GmailLogin:
    def __init__(self, config, driver):
        self.driver = driver
        self.config = config

    path = '/mail'

    # locators
    input_email_id = "identifierId"
    input_password_name = "password"
    button_next_xpath = '//span[text()="Next"]'

    def navigate(self):
        url = self.config['APPLICATION']['host']+ self.path
        self.driver.get(url)

    def sign_in(self, _email, _password):
        self.driver.find_element_by_id(self.input_email_id).send_keys(_email)
        self.driver.find_element_by_xpath(self.button_next_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_name(self.input_password_name).send_keys(_password)
        self.driver.find_element_by_xpath(self.button_next_xpath).click()