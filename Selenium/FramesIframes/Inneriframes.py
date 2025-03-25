import time

from selenium import webdriver
from selenium.webdriver.common.by import  By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
innerframe=driver.find_element(By.XPATH,"//iframe[@style='float: left;height: 250px;width: 400px']")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
time.sleep(5)
driver.close()