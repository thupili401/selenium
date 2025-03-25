import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
title1=driver.title   # To print Title
print(title1)
url=driver.current_url   #to print Current URL
print(url)
driver.quit()