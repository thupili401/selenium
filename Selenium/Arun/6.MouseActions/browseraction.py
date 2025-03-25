import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'compendiumdev')]").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
driver.quit()