
# Title
test-automation-kobiton

# Description
These are samples of how to use Python to run Automation Test with Selenium and on KOBITON.

### 1. SetUp
- Kobiton Credentials
- Access <https://portal.kobiton.com/> with your account
- Get your username & API Key
- Set your username & API Key & KOBITON_SERVER_URL

```
USERNAME = os.environ.get("USERNAME")
API_KEYS = os.environ.get("API_KEYS")
KOBITON_SERVER_URL = "https://" + USERNAME + ":" + API_KEYS + "@api.kobiton.com/wd/hub"

```

# Resources
<https://kobiton.com/>

<https://api.kobiton.com/docs/>

<https://github.com/kobiton/samples/tree/master/python>


