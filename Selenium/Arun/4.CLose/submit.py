import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://tutorialsninja.com/demo/index.php?route=account/login')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='email']").submit()
time.sleep(5)