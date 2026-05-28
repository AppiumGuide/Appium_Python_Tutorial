#Single-Line Options Creation/Initialization Approach

from appium import webdriver
from appium.options.android import UiAutomator2Options

driver=webdriver.Remote('http://127.0.0.1:4723',options=UiAutomator2Options.load_capabilities
                        ({
                            "platformname":"android",
                            "automationname":"uiautomator2"
                        }))