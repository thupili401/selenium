import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/frame")
driver.switch_to.frame("firstFr")
driver.find_element(By.XPATH,"//*[@name='fname']").send_keys("Sreekanth")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@name='lname']").send_keys("Reddy")
time.sleep(3)
childframe=driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")
driver.switch_to.frame(childframe)
driver.find_element(By.XPATH,"//*[@name='email']").send_keys("abc@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@name='email']").clear()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"//*[@name='fname']").clear()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@name='lname']").clear()
driver.close()