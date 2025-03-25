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

# Set implicit wait
driver.implicitly_wait(10)

# Begin app navigation and login
driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.embibe.embibelens:id/tvNext"]').click()
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvNext').click()
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/et_email_id').send_keys('9912866236')
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvSignInToggle').click()
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/et_password').send_keys('Embibe@123')
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvGetOtp').click()

# Post-login navigation
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/ivgrid4').click()
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/txtProceed').click()

# Handle pop-up and select a topic
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvGotItFromSubjectFilterInfo').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.embibe.embibelens:id/wordTV" and @text="Photosynthesis"]').click()

# Navigate through multiple screens using a loop
try:
    for _ in range(4):
        driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvNext').click()
except:
    print("Already given")
# Handle "Got It" and navigation back
driver.find_element(AppiumBy.ID, 'tvGotIt').click()
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/back_arrow').click()
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/backAndFlashIV').click()

# Handle permissions if prompted
try:
    driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
    driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_all_button').click()
except:
    print("Permissions already granted or not prompted.")

# Additional "Got It" screen and repeated navigation
driver.find_element(AppiumBy.ID, 'com.embibe.embibelens:id/tvGotIt').click()
try:
    for _ in range(5):
        driver.find_element(AppiumBy.ID, "com.embibe.embibelens:id/tvNext").click()
except:
    print("Already given")
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/optionsIV').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvUpgrade').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/subscription_TV').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/challenges_TV').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/ivClose').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/change_goals_TV').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="School Exams"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="CBSE"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="10th CBSE"]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvDone').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/optionsIV').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvChangeLanguage').click()
driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.embibelens:id/rvLanguage"]/android.widget.RelativeLayout[2]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvChangeLanguage').click()
driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.embibelens:id/rvLanguage"]/android.widget.RelativeLayout[1]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvReport').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="Problem after scanning of image"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="Expected keyword is missing."]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvConfirm').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/etKeyword').send_keys('Test')
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/etName').send_keys('Test')
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/etDescription').send_keys('Test')
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvReport').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvGoback').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvBookmarks').click()
driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.embibe.embibelens:id/rvBookmarks"]/android.widget.RelativeLayout[1]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/iv_back').click()
driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.embibe.embibelens:id/ivUnbookmark"])[2]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvSupport').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/section_text" and @text="What is EMBIBE Lens?"]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/ivClose').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/terms_of_services_TV').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/privacypolicy_TV').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()
#Timeline click
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/ivHistory').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/back_arrow').click()

#voice search
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvVoiceSearch').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvHint').send_keys("HumanHeart")
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.embibe.embibelens:id/tvSearchItem" and @text="Human Heart"]').click()
driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/rlAssetCardBorder').click()
try:
    for i in range (4):
        driver.find_element(AppiumBy.ID,'com.embibe.embibelens:id/tvNext').click()
except:
    print("Already Used")
driver.find_element(AppiumBy.ID, 'tvGotIt').click()


# Press Enter key (keycode 66) to confirm if needed
driver.press_keycode(66)

# Wait briefly and close the session
time.sleep(5)
driver.quit()
