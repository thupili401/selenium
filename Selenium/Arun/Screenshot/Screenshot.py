import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.save_screenshot("login3.png")
time.sleep(3)
driver.get_screenshot_as_file("Screenshot\\login_2.png") ##2nd method
driver.quit()
