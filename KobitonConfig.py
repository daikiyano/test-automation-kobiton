import os
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.keys import Keys
from AmazonSesSample import EmailService
from os.path import join, dirname
from dotenv import load_dotenv
import time
import unittest
import HTMLTestRunner
import random
import requests
import base64
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USERNAME = os.environ.get("USERNAME")
API_KEYS = os.environ.get("API_KEYS")
KOBITON_SERVER_URL = "https://" + USERNAME + ":" + API_KEYS + "@api.kobiton.com/wd/hub"
session_timeout = 120

def SetUpKobiton(self):
    FavoriteDevices = GetFavoriteDevices()
    for FavoriteDevice in FavoriteDevices['favoriteDevices']:
        if FavoriteDevice['isBooked'] == False:
            browserName = FavoriteDevice['installedBrowsers'][0]['name']
            deviceName = FavoriteDevice['deviceName']
            platformName = FavoriteDevice['platformName']
            platformVersion = FavoriteDevice['platformVersion']
            break
        else:
            continue
    desired_caps = {
        # The generated session will be visible to you only.
        'sessionName':        'Automation test session',
        'sessionDescription': '',
        'deviceOrientation':  'portrait',
        'captureScreenshots': True,
        'browserName':        browserName,
        'deviceGroup':        'KOBITON',
        # For deviceName, platformVersion Kobiton supports wildcard
        # character *, with 3 formats: *text, text* and *text*
        # If there is no *, Kobiton will match the exact text provided
        'deviceName':         deviceName,
        'platformName':       platformName,
        'platformVersion':    platformVersion
    }
    if desired_caps["platformName"] == "Android":
        self.driver = webdriver.Remote(KOBITON_SERVER_URL,desired_caps)
        self.driver.implicitly_wait(session_timeout)
        kobitonSessionId = self.driver.desired_capabilities.get('kobitonSessionId')
        print("https://portal.kobiton.com/sessions/%s" % (kobitonSessionId))
    elif desired_caps["platformName"] == "iOS":
        self.driver = webdriver.Remote(KOBITON_SERVER_URL, desired_caps)
        self.driver.implicitly_wait(session_timeout)
        kobitonSessionId = self.driver.desired_capabilities.get('kobitonSessionId')
        print("https://portal.kobiton.com/sessions/%s" % (kobitonSessionId))
        print(GetDevice())
        getTestResult(kobitonSessionId)

def GetFavoriteDevices():
    api_key = (USERNAME + ':' + API_KEYS)
    auth = base64.b64encode(api_key.encode())
    headers = {
    'Authorization': 'Basic ' + auth.decode(),
    'Accept': 'application/json'
    }
    response = requests.get('https://api.kobiton.com/v1/devices', params={

    }, headers = headers)
    data = response.json()
    return data

    
def QuitKobiton(self):
    self.driver.quit()
    kobitonSessionId = self.driver.desired_capabilities.get('kobitonSessionId')
    getTestResult(kobitonSessionId)

def getTestResult(kobitonSessionId):
    api_key = (USERNAME+ ':' + API_KEYS)
    auth = base64.b64encode(api_key.encode())
    print(auth)
    headers = {
            'Authorization': 'Basic ' + auth.decode(),
            'Accept': 'application/json'
            }
    response = requests.get('https://api.kobiton.com/v1/sessions/' + str(kobitonSessionId), params={
    }, headers = headers)
    data = response.json()
    EmailService().send_result_mail(data,kobitonSessionId)
    



