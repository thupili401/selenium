import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(5)
con_alerts=driver.switch_to.alert
time.sleep(5)
print(con_alerts.text)
#con_alerts.accept()
con_alerts.dismiss()
time.sleep(5)
driver.find_element(By.XPATH,"//a[text()='Elemental Selenium']").click()
time.sleep(5)
driver.quit()