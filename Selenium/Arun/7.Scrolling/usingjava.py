import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")
button=driver.find_element(By.XPATH,"//i[@class='interLink icon icon-down']")
driver.execute_script("arguments[0].scrollIntoView(true)",button)
time.sleep(3)
driver.close()