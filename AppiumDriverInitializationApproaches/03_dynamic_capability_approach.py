#Dynamic Capability approach for Appium driver/session intialization/creation

from appium import webdriver
from appium.options.android import UiAutomator2Options

options=UiAutomator2Options()

options.set_capability("platformname","Android")
options.set_capability("automationname","UiAutomator2")

driver=webdriver.Remote('http://127.0.0.1:4723',options=options)