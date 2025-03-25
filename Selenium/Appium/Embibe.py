import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

desired_caps= dict(
    deviceName='Android',
    platformName='Android',
    automationName='UIAutomator2',
    appActivity='com.embibe.jioembibe.mobile.LandingActivity',
    appPackage='com.embibe.student'

)
option = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=option)
time.sleep(5)