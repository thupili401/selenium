from datetime import time
from time import sleep

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


desired_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    # appActivity = 'com.embibe.teachlite.MainActivity',
    # appPackage ='com.embibe.schoolcensus',
    automationName = 'UIAutomator2',
    browserName = 'Chrome',
    # chromedriver_autodownload=True
    chromedriverExecutable = '/Users/sreekantht/PycharmProjects/Selenium/chromedriver'


)

option = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=option)
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(AppiumBy.XPATH,"//textarea[@name='q']").send_keys("thupili sreekanth reddy")
sleep(3)
driver.close()


