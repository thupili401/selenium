import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
driver.find_element(By.XPATH,"//a[contains(text(),'SeleniumTutorial')]").click()
time.sleep(5)
driver.close()  # it will close parent window
driver.quit() # close all the windows
time.sleep(5)