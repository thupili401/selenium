import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.find_element(By.XPATH,"//div[@class='labelCalendarContainer']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='labelCalendarContainer']").send_keys("18082024")
time.sleep(3)

time.sleep(3)
