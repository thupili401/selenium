import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()
time.sleep(10)
driver.close()#it will close previous window
driver.quit()# it close multiple windows at a time