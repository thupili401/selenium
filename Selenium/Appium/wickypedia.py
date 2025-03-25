from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy



desired_caps=dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome',
    automationName='UIAutomator2',
    chromedriverExecutable='/Users/sreekantht/PycharmProjects/Selenium/chromedriver'

)
option = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=option)
driver.get('https://www.wikipedia.org/')
driver.find_element(AppiumBy.XPATH,"//input[@id='searchInput']").send_keys("Thupili SreekanthReddy")
driver.find_element(AppiumBy.XPATH,"//button[@class='pure-button pure-button-primary-progressive']").click()
sleep(5)
driver.quit()