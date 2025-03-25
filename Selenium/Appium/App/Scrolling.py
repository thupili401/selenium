import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
desired_cap6=dict(
    deviceName='Android',
    platformName='Android',
    automationName='UIAutomator2',
    appActivity='com.google.android.apps.contacts.activities.ContactSelectionActivity',
    appPackage='com.google.android.contacts'
)
option = UiAutomator2Options().load_capabilities(desired_cap6)
driver = webdriver.Remote('http://127.0.0.1:4723', options=option)
driver.implicitly_wait(20)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Cnu").instance(0))').click()
time.sleep(5)
driver.quit()