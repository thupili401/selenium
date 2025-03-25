import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://embibe.com/")
driver.execute_script('alert("Sreekanth is Bad boy")')
time.sleep(3)
driver.quit()