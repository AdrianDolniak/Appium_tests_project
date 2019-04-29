#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from appium import webdriver



class Testowanie_aplikacji_Contacts(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.1',
            'avd': 'Nexus5X',
            'deviceName': 'emulator-5554',
            'language': 'en',
            'locale': 'en',
            'automationName': 'UiAutomator2',
            'appPackage': 'com.android.contacts',
            'appActivity': 'com.android.contacts.activities.PeopleActivity',
            'noReset': False
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)


    def tearDown(self):
        self.driver.quit()


    def test_add_contact(self):
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Create new contact"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text="CANCEL"]').click()
        f_name = self.driver.find_element_by_xpath('//android.widget.EditText[@text="First name"]')
        f_name.send_keys('Adam')
        l_name = self.driver.find_element_by_xpath('//android.widget.EditText[@text="Last name"]')
        l_name.send_keys('Nowak')
        p_number = self.driver.find_element_by_xpath('//android.widget.EditText[@text="Phone"]')
        p_number.send_keys('555666777')
        email = self.driver.find_element_by_xpath('//android.widget.EditText[@text="Email"]')
        email.send_keys('adamnowak@gmail.com')
        self.driver.find_element_by_xpath('//android.widget.Button[@text="SAVE"]').click()
        name = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="Adam Nowak"]').get_attribute('text')
        self.assertEqual(name, 'Adam Nowak')
        p_number = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="(555) 666-777"]').get_attribute('text')
        self.assertEqual(p_number, '(555) 666-777')
        email = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="adamnowak@gmail.com"]').get_attribute('text')
        self.assertEqual(email, 'adamnowak@gmail.com')
        self.driver.back()
        contact = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Adam Nowak"]')
        self.assertTrue(contact.is_displayed())


    def test_del_contact(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Adam Nowak"]').click()
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="More options"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Delete"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text="DELETE"]').click()
        empty_list = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="Your contacts list is empty"]').get_attribute('text')
        self.assertEqual(empty_list, 'Your contacts list is empty')



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testowanie_aplikacji_Contacts)
    unittest.TextTestRunner(verbosity=2).run(suite)
