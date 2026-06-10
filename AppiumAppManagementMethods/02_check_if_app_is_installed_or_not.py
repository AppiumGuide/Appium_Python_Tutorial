'''
=========================================================
Appium Concepts: To Check Whether an App Is Installed or Not
Method: is_app_installed()
=========================================================

Description:
Learn how to verify whether an application is installed or not on a mobile device
using Appium's built-in `is_app_installed()` method.

Author : Ramesh Kodumuru
Channel: AppiumGuide
Email  : appiumguide@gmail.com
=========================================================
'''
from appium import webdriver
from appium.options.android import UiAutomator2Options

options=UiAutomator2Options()

options.platform_name="Android"
options.automation_name="UiAutomator2"

driver=webdriver.Remote("http://127.0.0.1:4723",options=options)

#To verify the wdio demo app is installed or not

status=driver.is_app_installed("com.wdiodemoapp")

#print("WDIODemo app is installed or not -",status)

if driver.is_app_installed("com.wdiodemoapp"):
    print("WDIODemo app is already installed",status)
else:
    print("WDIODemo app is not installed")
    print("WDIO Demoapp status before instaling: ",status)
    driver.install_app("C:/Users/SWETHARAMESH/Desktop/AppiumGuide/Appium_Python_Tutorial/apk_files/android.wdio.native.app.v1.0.8.apk")
    print("WDIODEmo app is sucessfully installed")
    status=driver.is_app_installed("com.wdiodemoapp")
    print("WDIO Demoapp status after installing: ",status)