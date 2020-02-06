import os
import sys
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.keys import Keys
from AmazonSesSample import EmailService
from os.path import join, dirname
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import time
import unittest
import random
import requests
import base64
import json
import atexit
import shutil


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
    # Delete file in the report folder
    target_dir = 'report'
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)  
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
    try:
        browserName
    except:
        print('Device is no available')

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

    # After finising program and generating Xml file as results, fetchTestResult() going to run.
    atexit.register(fetchTestResult, session_list)
    
    


###########################################################################
###############Get Test Result and Send mail###############################
###########################################################################


path = os.getcwd()
files = os.listdir(path)

# fond file witch match 'test_'
test_files = [file for file in files if 'test' in file]
files_count = len(test_files)
count = 0
# make two-dimensional list
result_lists = [[] for i in range(files_count)]

email_text = "<table border='1'><tr><th>File name</th><th>Status</th><th>Device Name</th><th>Session URL</th><th>result</th></tr>"
def fetchTestResult(kobitonSessionIds):
    for kobitonSessionId in kobitonSessionIds:
        print("https://portal.kobiton.com/sessions/%s" % (kobitonSessionId))
        global count
        global email_text
        global files
        api_key = (USERNAME+ ':' + API_KEYS)
        auth = base64.b64encode(api_key.encode())
        headers = {
                'Authorization': 'Basic ' + auth.decode(),
                'Accept': 'application/json'
                }
        response = requests.get('https://api.kobiton.com/v1/sessions/' + str(kobitonSessionId), params={
        }, headers = headers)
        data = response.json()

        xml_files = os.listdir(path + "/report")
        result_lists[count].append(test_files[count])
        result_lists[count].append(data['state'])
        result_lists[count].append(data['executionData']['desired']['deviceName'])
        result_lists[count].append("https://portal.kobiton.com/sessions/"+ str(kobitonSessionId))
        
        for xml_file in xml_files:
            if  test_files[count][0:-3] in xml_file:
                with open("report/" + xml_file) as f:
                    soup = BeautifulSoup(f, 'xml')
                for e in soup.find_all('error'):
                    result_lists[count].append(e)
        count += 1
        print(count)
        if count == files_count:
            for result_list in result_lists:
                print(result_list[0])
                if len(result_list) == 4:
                    email_text += "<tr bgcolor='79BBFF'><td>" + result_list[0] + "</td>"
                    email_text += "<td>" + result_list[1] + "</td>"
                    email_text += "<td>" + result_list[2] + "</td>"
                    email_text += "<td>" + result_list[3] + "</td>"
                    email_text += "<td>Passed</td></tr>"
                else:
                    email_text += "<tr bgcolor='#F56C6C'><td>" + result_list[0] + "</td>"
                    email_text += "<td>" + result_list[1] + "</td>"
                    email_text += "<td>" + result_list[2] + "</td>"
                    email_text += "<td>" + result_list[3] + "</td>"
                    email_text += "<td>Failed</td></tr>"
                    email_text += "<tr><td colspan='5'>Error Description</td></tr>"
                    email_text += "<tr><td bgcolor='#F56C6C' colspan='5'>" + str(result_list[4]) + "</td></tr>"    
            email_text += "</table>"
            EmailService().send_result_mail(email_text,kobitonSessionId)  
        else:
            print("Test is still in progress...")
        

    

        

   

    

        

   
