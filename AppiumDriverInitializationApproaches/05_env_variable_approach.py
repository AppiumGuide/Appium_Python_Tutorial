#Using “Environment Variables” Approach for Appium driver/session intialization/creation

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

options=UiAutomator2Options()

options.platform_name=os.getenv("PLATFORM_NAME","Android")
options.automation_name=os.getenv("AUTOMATION_NAME","UiAutomator2")

driver=webdriver.Remote('http:127.0.0.1:4723',options=options)