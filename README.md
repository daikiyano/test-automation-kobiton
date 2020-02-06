
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
KobitonConfig.py
USERNAME = os.environ.get("USERNAME")
API_KEYS = os.environ.get("API_KEYS")
KOBITON_SERVER_URL = "https://" + USERNAME + ":" + API_KEYS + "@api.kobiton.com/wd/hub"

```

```
AmazonSesSample.py 

SENDER = "YOUR EMAIL"
RECIPIENT = "YOUR EMAIL"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

```



- set up

```
from selenium import webdriver
import KobitonConfig
import unittest
import xmlrunner


def setUp(self):
        KobitonConfig.SetUpKobiton(self)
    
def tearDown(self):
    KobitonConfig.QuitKobiton(self)
        
```


# Resources
<https://kobiton.com/>

<https://api.kobiton.com/docs/>

<https://github.com/kobiton/samples/tree/master/python>



