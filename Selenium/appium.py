import time

from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = dict(


         deviceName = "Android",
         platformName = "Android",
         appPackage = "com.zeptoconsumerapp",
         appActivity = "com.zeptoconsumerapp.MainActivity",
         automationName = "UIAutomator2",
         noReset = True
)

options = UiAutomator2Options().load_capabilities(desired_cap)

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

time.sleep(5)


driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Phone Number"]').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Phone Number"]').send_keys("9035371071")
time.sleep(5)
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.zeptoconsumerapp:id/welcome-continue-button"]').click()
time.sleep(20)
# driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@resource-id='com.zeptoconsumerapp:id/homepage-search-box']/android.view.ViewGroup/android.widget.TextView").click()
time.sleep(5)

driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Search for']").send_keys("Paneer")

driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.zeptoconsumerapp:id/autosuggest-text-Paneer'])[3]").click()