#Capabilities Loading Approach for Appium driver/session creation

from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_caps={
    "platformname":"Android",
    "automationname":"UiAutomator2"
}

options=UiAutomator2Options().load_capabilities(desired_caps)

driver=webdriver.Remote('http://127.0.0.1:4723',options=options)


