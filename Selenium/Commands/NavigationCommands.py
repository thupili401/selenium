import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.embibe.com/")
time.sleep(5)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(5)

driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()