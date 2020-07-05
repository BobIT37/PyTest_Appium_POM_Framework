import pytest
import unittest
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=5)
    def test_enterDataInEditBox(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()

    @pytest.mark.run(order=4)
    def test_openLoginScreen(self):
        self.bp.keyCode(4)
        self.gt.clickLoginBotton()
        self.gt.enterEmail()
        self.gt.enterPassword()
        self.gt.clickOnLoginB()
        self.gt.verifyAdminScreen()

    @pytest.mark.run(order=3)
    def test_loginFailMethod(self):
        cl.allureLogs("App Opened")
        self.gt.clickLoginBotton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickOnLoginB()
        self.gt.verifyAdminScreen()
