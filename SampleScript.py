#Sample Script to Validate the "Appium Setup" with VS Code

from appium import webdriver
from appium.options.android import UiAutomator2Options

options=UiAutomator2Options()

options.platform_name="Android"
options.automation_name="UiAutomator2"

driver=webdriver.Remote('http://127.0.0.1:4723',options=options)

#To Fetch the Current Session Id of the current run/execution
print("Current Session Id of this run : ",driver.session_id)