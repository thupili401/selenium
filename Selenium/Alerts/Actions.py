import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
alert=driver.switch_to.alert
print(alert.text)
#alert.send_keys('Welcome')
#alert.accept()
alert.dismiss()
time.sleep(5)