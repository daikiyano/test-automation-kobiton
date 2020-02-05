import os
import sys
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.keys import Keys
from AmazonSesSample import EmailService
from os.path import join, dirname
from dotenv import load_dotenv
import time
import unittest
import random
import requests
import base64
import json
from time import sleep
import atexit
from bs4 import BeautifulSoup



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
USERNAME = os.environ.get("USERNAME")
API_KEYS = os.environ.get("API_KEYS")
KOBITON_SERVER_URL = "https://" + USERNAME + ":" + API_KEYS + "@api.kobiton.com/wd/hub"
session_timeout = 120

###############FetchFavoriteDevices##############################
def FetchFavoriteDevices():
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

def SetUpKobiton(self):
    FavoriteDevices = FetchFavoriteDevices()
    for FavoriteDevice in FavoriteDevices['favoriteDevices']:
        if FavoriteDevice['isBooked'] == False and FavoriteDevice['isOnline'] == True:
            browserName = FavoriteDevice['installedBrowsers'][0]['name']
            deviceName = FavoriteDevice['deviceName']
            platformName = FavoriteDevice['platformName']
            platformVersion = FavoriteDevice['platformVersion']
            print(deviceName)
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
        'groupId':            944,
        'deviceName':         deviceName,
        'platformName':       platformName,
        'platformVersion':    platformVersion
    }

    self.driver = webdriver.Remote(KOBITON_SERVER_URL,desired_caps)
    self.driver.implicitly_wait(session_timeout)
    kobitonSessionId = self.driver.desired_capabilities.get('kobitonSessionId')
    print("https://portal.kobiton.com/sessions/%s" % (kobitonSessionId))
   

session_list = []
###############Finish Test on Kobiton#################################
def QuitKobiton(self):
    self.driver.quit()
    kobitonSessionId = self.driver.desired_capabilities.get('kobitonSessionId')
    session_list.append(kobitonSessionId)
    print(session_list)
    atexit.register(fetchTestResult, session_list)
    

###########################################################################
###############Get Test Result and Send mail###############################
###########################################################################



path = os.getcwd()
files = os.listdir(path)

# fond file witch match 'test_'
test_files = [file for file in files if 'test_' in file]
files_count = len(test_files)
count = 0
# make two-dimensional list
result_lists = [[] for i in range(files_count)]


email_text = "<table border='1'><tr><th>File name</th><th>Status</th><th>Device Name</th><th>Session URL</th><th>result</th></tr>"
def fetchTestResult(kobitonSessionIds):
    for kobitonSessionId in kobitonSessionIds:
        print("####################")
        print(kobitonSessionId)
        global count
        global email_text
        global files
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

        report_path = path + "/report"
        report_paths = os.listdir(report_path)
        result_lists[count].append(test_files[count])
        result_lists[count].append(data['state'])
        result_lists[count].append(data['executionData']['desired']['deviceName'])
        result_lists[count].append("https://portal.kobiton.com/sessions/"+ str(kobitonSessionId))
        for report_path in report_paths:
            if  test_files[count][0:-3] in report_path:
                print("######")
                print(report_path)
                with open("report/" + report_path) as f:
                    soup = BeautifulSoup(f, 'xml')
                for e in soup.find_all('error'):
                    print(e)
                    result_lists[count].append(e)
        count += 1
        print(count)
        if count == files_count:
            for result_list in result_lists:
                print(result_list[0])
                if len(result_list) == 4:
                    email_text += "<tr bgcolor='green'><td>" + result_list[0] + "</td>"
                    email_text += "<td>" + result_list[1] + "</td>"
                    email_text += "<td>" + result_list[2] + "</td>"
                    email_text += "<td>" + result_list[3] + "</td>"
                    email_text += "<td>Passed</td></tr>"
                else:
                    email_text += "<tr bgcolor='red'><td>" + result_list[0] + "</td>"
                    email_text += "<td>" + result_list[1] + "</td>"
                    email_text += "<td>" + result_list[2] + "</td>"
                    email_text += "<td>" + result_list[3] + "</td>"
                    email_text += "<td>Failed</td></tr>"
                    email_text += "<tr><td bgcolor='red' colspan='5'>" + str(result_list[4]) + "</td></tr>"    
            
            email_text += "</table>"
            EmailService().send_result_mail(email_text,kobitonSessionId)     
        else:
            print("Contunue Test")
        

    

        

   
