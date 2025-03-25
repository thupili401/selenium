import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
info_alert=driver.switch_to.alert
print(info_alert.text)
#info_alert.accept()
info_alert.dismiss()
driver.find_element(By.XPATH,"//a[text()='Elemental Selenium']").click()
time.sleep(5)
driver.quit()