from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
desired_cap3=dict(
    deviceName='Android',
    platformName='Android',
    app='/Users/sreekantht/PycharmProjects/Selenium/Selenium/Appium/App/lens.apk'



)

option = UiAutomator2Options().load_capabilities(desired_cap3)
driver = webdriver.Remote('http://127.0.0.1:4723', options=option)