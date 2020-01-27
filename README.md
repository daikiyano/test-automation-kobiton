
# Title
test-automation-kobiton

# Description
These are samples of how to use Python to run Automation Test with Selenium and on KOBITON.

### 1. SetUp(General)
- Kobiton Credentials
- Access <https://portal.kobiton.com/> with your account
- Get your username & API Key
- Set your username & API Key & KOBITON_SERVER_URL

```
USERNAME = os.environ.get("USERNAME")
API_KEYS = os.environ.get("API_KEYS")
KOBITON_SERVER_URL = "https://" + USERNAME + ":" + API_KEYS + "@api.kobiton.com/wd/hub"

```
- set up

```
def SetUpKobiton(self):
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
        getTestResult(kobitonSessionId)

def QuitKobiton(self):
    self.driver.quit()
    kobitonSessionId = self.driver.desired_capabilities.get('kobitonSessionId')
    getTestResult(kobitonSessionId)

```

- set your desired device

```
desired_caps = {
  # The generated session will be visible to you only.
  'sessionName':        'Automation test session',
  'sessionDescription': '',
  'deviceOrientation':  'portrait',
  'captureScreenshots': True,
  'browserName':        'chrome',
  'deviceGroup':        'KOBITON',
  # For deviceName, platformVersion Kobiton supports wildcard
  # character *, with 3 formats: *text, text* and *text*
  # If there is no *, Kobiton will match the exact text provided
  'deviceName':         'Galaxy A8(2016)',
  'platformName':       'Android',
  'platformVersion':    '7.0'
}


```

# Resources
<https://kobiton.com/>

<https://api.kobiton.com/docs/>

<https://github.com/kobiton/samples/tree/master/python>



