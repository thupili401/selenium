import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(5)
promt_alert=driver.switch_to.alert
time.sleep(5)
print(promt_alert.text)
promt_alert.send_keys("Hi sreekanth")
time.sleep(3)
#promt_alert.accept()
promt_alert.dismiss()
time.sleep(3)
driver.quit()