import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
driver.find_element(By.ID,"ta1").send_keys("sreekanth")
driver.find_element(By.XPATH,"//a[contains(.,'compendiumdev')]").click()
driver.back()
driver.find_element(By.ID,"ta1").clear()
time.sleep(3)
driver.close()