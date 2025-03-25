import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='fname']").clear()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='fname']").send_keys('Pramara')
time.sleep(5)
driver.close()
