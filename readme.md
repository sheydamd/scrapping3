# Typekadeh Login Automation with Selenium
This project is a simple Python automation script using Selenium and Microsoft Edge.  
It opens the [Typekadeh](https://typekadeh.com/) website, clicks on the login tab, and automatically fills your email, username, and password to log in to your account.

##  Requirements

To run this script, you’ll need the following:
- Python packages:
  - selenium
- having account:
    - creat new account by using your gmail or phone in this site

##  Installation

### 1. Create and activate virtual environment (optional but recommended)

Windows :
`bash

python -m venv .venv

.venv\Scripts\activate

- install selenium by using:
    - pip install selenium

and you should import:
```python
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
```
# Running the Script

Make sure your virtual environment is activated, then run:

python typekadeh.py

# Script Overview

Launches Microsoft Edge using Selenium

Navigates to typekadeh.com

Clicks the login button

Switches to login tab

Fills in:

Email: youremail@gmail.com

Username: your username

Password: ******


Clicks the login/submit button

Waits to observe the result

## Technical Notes

The script uses time.sleep() to pause for page load

It safely handles element finding via tag names and class names.
