import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
desired_cap1=dict(
    deviceName='Android',
    platformName='Android',
    automationName='UIAutomator2',
    appActivity='com.android.calculator2.Calculator',
    appPackage='com.oneplus.calculator'
)
option = UiAutomator2Options().load_capabilities(desired_cap1)
driver = webdriver.Remote('http://127.0.0.1:4723', options=option)
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.oneplus.calculator:id/digit_9"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.oneplus.calculator:id/img_op_mul"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.oneplus.calculator:id/digit_2"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.oneplus.calculator:id/img_eq"]').click()
result=driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.oneplus.calculator:id/result"]')
print(result.text)
time.sleep(5)
driver.quit()