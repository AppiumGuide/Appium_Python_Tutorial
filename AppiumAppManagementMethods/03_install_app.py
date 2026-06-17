'''
=========================================================
Appium Concepts: To install App (i.e apk file) during runtime
Method: install_app()
=========================================================

Description:
Learn how to install the app(i.e apk file) during runtime
using Appium's built-in `install_app()` method.

Author : Ramesh Kodumuru
Channel: AppiumGuide
Email  : appiumguide@gmail.com
=========================================================
'''
from appium import webdriver
from appium.options.android import UiAutomator2Options

options=UiAutomator2Options()

options.platform_name="android"
options.automation_name="UiAutomator2"

driver=webdriver.Remote("http://127.0.0.1:4723",options=options)

if driver.is_app_installed("com.wdiodemoapp"):
    print("WDIO Demo app is already installed")
else:
    print("WDIO Demo app is not installed,will be installed now")
    driver.install_app("C:/Users/SWETHARAMESH/Desktop/AppiumGuide/Appium_Python_Tutorial/apk_files/android.wdio.native.app.v1.0.8.apk")
    print("Successfully installed the WDIO Demo app")