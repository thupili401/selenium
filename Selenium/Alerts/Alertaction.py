import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.close()