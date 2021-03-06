
# Title
test-automation-kobiton

# Description
These are samples of how to use Python to run Automation Test with Selenium and on KOBITON.

<<<<<<< HEAD
### 1. SetUp(General)
- install python library 

```
pip install -r requirements.txt
```

=======
# Kobiton
- Set desired devices as favorite devices on Kobiton.

<img width="1235" alt="Screen Shot 2020-02-06 at 18 15 34" src="https://user-images.githubusercontent.com/36895565/73956066-0f668180-490d-11ea-884f-8c60d6913765.png">


# SetUp
>>>>>>> 9b7860bc35ed4f048f5e7b27296ac571a9900bd9
- Kobiton Credentials
- Access <https://portal.kobiton.com/> with your account
- Get your username & API Key
- Set your username & API Key & KOBITON_SERVER_URL on KobitonConfig.py

```
KobitonConfig.py
USERNAME = os.environ.get("USERNAME")
API_KEYS = os.environ.get("API_KEYS")
KOBITON_SERVER_URL = "https://" + USERNAME + ":" + API_KEYS + "@api.kobiton.com/wd/hub"

```

- Get your ACCESS_KEY & AWS_SECRET_ACCESS_KEY on AWS
- Set your ACCESS_KEY & AWS_SECRET_ACCESS_KEY & your Email on AmazonSesSample.py 


```
AmazonSesSample.py 

SENDER = "YOUR EMAIL"
RECIPIENT = "YOUR EMAIL"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

```

<<<<<<< HEAD
File name should be test*.py


=======
>>>>>>> 9b7860bc35ed4f048f5e7b27296ac571a9900bd9
```
from selenium import webdriver
import KobitonConfig
import unittest
import xmlrunner


def setUp(self):
        KobitonConfig.SetUpKobiton(self)
    
def tearDown(self):
    KobitonConfig.QuitKobiton(self)
    
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='reports'),failfast=False, buffer=False, catchbreak=False)
        
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

