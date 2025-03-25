from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
mywait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get('https://www.google.com/')
var=driver.find_element(By.NAME,'q')
var.send_keys('selenium')
var.submit()

var=mywait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
var.click()
driver.close()