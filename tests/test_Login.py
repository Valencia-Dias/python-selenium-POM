from config.config import TestData
from pages.loginPage import LoginPage
from tests.test_Base import BaseTest


class Test_Login(BaseTest):

    def __init__(self):
        self.driver = None

    def test_login(self):
        pass
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(TestData.username, TestData.password)
