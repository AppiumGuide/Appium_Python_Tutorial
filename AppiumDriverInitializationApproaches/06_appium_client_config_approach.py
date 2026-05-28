#Client Configuration Approach for Appiun Driver Intialization/session creation

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.client_config import AppiumClientConfig

options=UiAutomator2Options()

options.platform_name="Android"
options.automation_name="UiAutomator2"

client_config=AppiumClientConfig(
    remote_server_addr="http://127.0.0.1:4723"
)

driver=webdriver.Remote(client_config=client_config,options=options)