
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


<<<<<<< HEAD

- set up
=======
# set up

File name should be test*.py
>>>>>>> 5236fd286d34c6673fd37ee0eed9a95d1444d3a9

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

# Command-line

```
python -m xmlrunner discover -o report

or

python [file name]

```
# Result list as Email


<img width="1084" alt="Screen Shot 2020-02-06 at 11 17 19" src="https://user-images.githubusercontent.com/36895565/73955363-e7c2e980-490b-11ea-83f7-c2925a75641b.png">

# Resources
<https://kobiton.com/>

<https://api.kobiton.com/docs/>

<https://github.com/kobiton/samples/tree/master/python>

<https://github.com/xmlrunner/unittest-xml-reporting>

