#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class Testowanie_aplikacji_HBOGO(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.1',
            'avd': 'Nexus5X',
            'deviceName': 'emulator-5554',
            'language': 'pl',
            'locale': 'pl',
            'automationName': 'UiAutomator2',
            'otherApps': PATH('/home/adi/Appium/apps/HBO GO_v5.6.0_apkpure.com.apk'),
            'appPackage': 'eu.hbogo.android',
            'appActivity': 'eu.hbogo.android.setup.activity.SetUpActivity',
            'noReset': False
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)


    def tearDown(self):
       self.driver.quit()


    def test_invalid_user_abonenci(self):
        app_title = self.driver.find_element_by_xpath(
            '//android.widget.ImageView[@resource-id="eu.hbogo.android:id/iv_country_selector_logo"]')
        self.assertTrue(app_title.is_displayed())
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Polska"]').click()
        checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
        self.assertTrue(checkbox.is_enabled())
        self.driver.find_element_by_xpath('//android.widget.Button[@text="NASTĘPNY"]').click()
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="Abonenci HBO GO u operatorów"]').click()
        self.driver.find_element_by_class_name('android.widget.Spinner').click()
        nc_plus = self.driver.find_elements_by_class_name('android.widget.CheckedTextView')
        nc_plus[2].click()
        text_fields = self.driver.find_elements_by_class_name('android.widget.EditText')
        text_fields[0].send_keys('adamnowak@gmail.com')
        text_fields[1].send_keys('QAZwsx1!')
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zaloguj się"]').click()
        info = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Błędna nazwa użytkownika lub hasło (12.20)"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Błędna nazwa użytkownika lub hasło (12.20)', info)


    def test_user_not_in_database_abonenci(self):
        app_title = self.driver.find_element_by_xpath(
            '//android.widget.ImageView[@resource-id="eu.hbogo.android:id/iv_country_selector_logo"]')
        self.assertTrue(app_title.is_displayed())
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Polska"]').click()
        checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
        self.assertTrue(checkbox.is_enabled())
        self.driver.find_element_by_xpath('//android.widget.Button[@text="NASTĘPNY"]').click()
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="Abonenci HBO GO u operatorów"]').click()
        self.driver.find_element_by_class_name('android.widget.Spinner').click()
        nc_plus = self.driver.find_elements_by_class_name('android.widget.CheckedTextView')
        nc_plus[2].click()
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zapomniałeś hasła?"]').click()
        sleep(2)
        text_fields = self.driver.find_elements_by_class_name('android.widget.EditText')
        text_fields[2].send_keys('adamnowak@gmail.com')
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Wyślij link resetu hasła"]').click()
        info = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc='
            '"Klient nie został znaleziony w bazie serwisu HBO GO. (4.65)"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Klient nie został znaleziony w bazie serwisu HBO GO. (4.65)', info)


    def test_user_not_in_database_subskrybenci(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Polska']").click()
        checkbox = self.driver.find_element_by_id('eu.hbogo.android:id/iv_tick')
        self.assertTrue(checkbox.is_enabled())
        self.driver.find_element_by_xpath('//android.widget.Button[@text="NASTĘPNY"]').click()
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="Subskrybenci"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Zapomniałeś hasła?"]').click()
        sleep(2)
        text_fields = self.driver.find_elements_by_class_name('android.widget.EditText')
        text_fields[2].send_keys('adamnowak@gmail.com')
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Wyślij link resetu hasła"]').click()
        info = self.driver.find_element_by_xpath(
            '//android.view.View[@content-desc="Wystąpił błąd podczas autentykacji użytkownika (12.99)"]').get_attribute(
            'contentDescription')
        self.assertEqual(u'Wystąpił błąd podczas autentykacji użytkownika (12.99)', info)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testowanie_aplikacji_HBOGO)
    unittest.TextTestRunner(verbosity=2).run(suite)
