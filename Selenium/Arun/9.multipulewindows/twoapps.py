import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://embibe.darwinbox.in/")
app1_title=driver.title
time.sleep(3)
print(app1_title)
driver.switch_to.new_window('tab') #to open in new tab
driver.switch_to.new_window('window') #to open in window
time.sleep(3)
driver.get("https://www.embibe.com/")
time.sleep(3)
app2_title=driver.title
print(app2_title)
driver.close()