import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities
desired_cap4 = dict(
    appName='Android',
    platformName='Android',
    automationName='UIAutomator2',
    appActivity='com.embibe.embibelens.ui.activities.LauncherActivity',
    appPackage='com.embibe.embibelens'
)

# Initialize options and driver
option = UiAutomator2Options().load_capabilities(desired_cap4)
driver = webdriver.Remote('http://127.0.0.1:4723', options=option)
driver.implicitly_wait(10)

# Function definitions

def login():
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.embibe.embibelens:id/tvNext"]').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvNext').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/et_email_id').send_keys('9912866236')
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvSignInToggle').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/et_password').send_keys('Embibe@123')
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvGetOtp').click()

def post_login_navigation():
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/ivgrid4').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/txtProceed').click()

def handle_permissions():
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'))
        ).click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_all_button'))
        ).click()
    except:
        print("Permissions already granted or not prompted.")

def navigate_topic():
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvGotItFromSubjectFilterInfo').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.embibelens:id/wordTV" and @text="Photosynthesis"]').click()

def repeat_navigation():
    try:
        for _ in range(4):
            driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvNext').click()
    except:
        print("Navigation through tvNext screens already completed")

def change_settings_and_report_issue():
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/optionsIV').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvUpgrade').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/back_arrow').click()

    # More navigation actions can follow here...
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvReport').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="Problem after scanning of image"]').click()
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="Expected keyword is missing."]').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvConfirm').click()
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/etKeyword').send_keys('Test')
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/etName').send_keys('Test')
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/etDescription').send_keys('Test')
    driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvReport').click()

# Running the main sequence
try:
    login()
    post_login_navigation()
    handle_permissions()
    navigate_topic()
    repeat_navigation()
    change_settings_and_report_issue()

    # Press Enter key (keycode 66) to confirm if needed
    driver.press_keycode(66)

finally:
    # Wait briefly and close the session
    time.sleep(5)
    driver.quit()
