from selenium.webdriver.common.by import By
from config.config import TestData
from pages import basePage


class LoginPage(basePage):
    username = (By.NAME, 'username')
    password = (By.NAME, 'password')


# constructor of the page class
def __init__(self, driver):
    super().__init__(driver)
    self.driver.get(TestData.base_url)


def do_login(self, username, password):
    self.do_send_keys(self.username, username)
    self.do_send_keys(self.password, password)
