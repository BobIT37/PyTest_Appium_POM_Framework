import pytest
import unittest

import utilities.CustomLogger as cl
from pages.ContactUsFormPage import ContactForm
from base.BasePage import BasePage

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()
        self.bp.screenShot("enterdata")

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
