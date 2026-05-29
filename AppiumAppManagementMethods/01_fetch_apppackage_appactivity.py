'''
 * Script Details - Appium Concepts : How to Get "appPackage" and "appActivity" during runtime(programmatically)
 * 
 * @author 'Ramesh Kodumuru' for AppiumGuide [appiumguide@gmail.com]
 '''
from appium import webdriver
from appium.options.android import UiAutomator2Options

options=UiAutomator2Options()

options.platform_name="Android"
options.automation_name="UiAutomator2"

driver=webdriver.Remote("http://127.0.0.1:4723",options=options)

# To fetch/get current app package

print("current app package details: ",driver.current_package)

# To fetch/get current app activity

print("current app activity details: ",driver.current_activity)