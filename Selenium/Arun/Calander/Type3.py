import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import  By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.guru99.com/test/")
driver.find_element(By.XPATH,"//input[@name='bdaytime']").send_keys("19121988")
driver.find_element(By.XPATH,"//input[@name='bdaytime']").send_keys(Keys.TAB)
driver.find_element(By.XPATH,"//input[@name='bdaytime']").send_keys("0732")
driver.find_element(By.XPATH,"//input[@name='bdaytime']").send_keys(Keys.TAB)
driver.find_element(By.XPATH,"//input[@name='bdaytime']").send_keys("AM")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)