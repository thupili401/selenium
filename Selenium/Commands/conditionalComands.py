import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
from  selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
var=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(var.is_enabled())
print(var.is_displayed())
time.sleep(5)
var1=driver.find_element(By.XPATH,"//input[@id='pollanswers-1']")
var2=driver.find_element(By.XPATH,"//input[@id='pollanswers-2']")
print(var1.is_selected())
print(var2.is_selected())
var1.click()
print(var1.is_selected())
print(var2.is_selected())
var2.click()
print(var1.is_selected())
print(var2.is_selected())