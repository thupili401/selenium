import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://omayo.blogspot.com/')
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @name='accessories']")
print(len(checkboxes))
for i in checkboxes:
    x=i.get_attribute('value')
    if x=='pen' or x=='bag':
        i.click()


time.sleep(10)
driver.close()
