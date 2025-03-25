import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://omayo.blogspot.com/')
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @name='accessories']")
for i in checkboxes:
    if i.is_selected():
        i.click()
time.sleep(5)
driver.close()
