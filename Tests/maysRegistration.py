# -*- coding: utf-8 -*-
import TestRunner as TestRunner
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re

class MaysRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.macys.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_mays_registration(self):
        print("=======Inside test_mays_registration test======")
        pass

    @unittest.skip("demonstrating skipping")
    def test_mays_login(self):
        print("=======Inside test_mays_login test======")

    @unittest.expectedFailure
    def test_expected_failure_test(self):
        self.fail("========demonstrating expectedFailure=====")

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print(unittest.TestResult)
        os.system("python /Users/swatidhoke/PycharmProjects/Automation_Frameworks/UI_Selenium_framework/Tests/sendmail.py")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MaysRegistration)
    unittest.TextTestRunner(verbosity=2).run(suite)