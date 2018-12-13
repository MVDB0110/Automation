# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random


class Adduser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_adduser(self):
        driver = self.driver
        driver.get("http://172.16.83.151/cms-simple/cms/")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("admin")
        driver.find_element_by_id("pw").clear()
        driver.find_element_by_id("pw").send_keys("admin")
        driver.find_element_by_id("pw").send_keys(Keys.ENTER)
        driver.find_element_by_link_text("Administration").click()
        driver.find_element_by_link_text("User administration").click()
        driver.find_element_by_link_text("Create user account").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("admin"+str(random.randint(1,100)))
        driver.find_element_by_id("pw").clear()
        driver.find_element_by_id("pw").send_keys("P@ssw0rd")
        driver.find_element_by_id("pw_r").clear()
        driver.find_element_by_id("pw_r").send_keys("P@ssw0rd")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Repeat password:'])[1]/following::button[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
