from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.google.com/')
var=driver.find_element(By.NAME,'q')
var.send_keys('selenium')
var.submit()
driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
driver.close()