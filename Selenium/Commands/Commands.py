import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.embibe.com/')
#Application commands
print(driver.title)
time.sleep(5)
print(driver.current_url)
print(driver.page_source)
time.sleep(5)
driver.quit()
#conditional comands
