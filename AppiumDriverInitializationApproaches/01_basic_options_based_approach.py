#Options Based Approach for Appium driver/session creation

from appium import webdriver
from appium.options.android import UiAutomator2Options

options=UiAutomator2Options()

options.platform_name="Android"
options.automation_name="UiAutomator2"

driver=webdriver.Remote('http://127.0.0.1:4723',options=options)

