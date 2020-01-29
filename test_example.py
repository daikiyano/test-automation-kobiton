from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HTMLTestRunner
import random
import KobitonConfig
import requests



class test_user_account(unittest.TestCase):
    @classmethod
    def setUp(self):
        KobitonConfig.SetUpKobiton(self)
    

    def test_account_login(self):
        self.driver.get("https://www.komazawa-u.ac.jp/")
        self.driver.find_element_by_css_selector('#keyWrap > nav > ul > li.vUser > a').click()
        self.driver.find_element_by_css_selector('#setEntryBase > div > ul > li:nth-child(1) > a').click()
        time.sleep(5)
        handle_array = self.driver.window_handles
        self.driver.switch_to.window(handle_array[-1])
        self.driver.find_element_by_id("username").send_keys('EMAIL')
        self.driver.find_element_by_id("password").send_keys("PASSWORD")
        self.driver.find_element_by_css_selector('#login > button').click()
    
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_css_selector('#sub > ul > li:nth-child(2) > a > img').click()
        time.sleep(10) 
        print(self.driver.current_url)
        handle_array = self.driver.window_handles
        self.driver.switch_to.window(handle_array[-1])
        self.driver.find_element_by_id("edit-name").send_keys("USER")
        self.driver.find_element_by_id("edit-pass").send_keys("PASSWORD")
        self.driver.find_element_by_id("edit-submit").click()
        time.sleep(10) 
       
       

    @classmethod
    def tearDown(self):
        KobitonConfig.QuitKobiton(self)
   

if __name__ == '__main__':
    unittest.main()
   

