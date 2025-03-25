import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_actions=webdriver.ChromeOptions()
Chrome_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://docs.oracle.com/javase/8/docs/api/")
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"//a[contains(.,'Description')]").click()
time.sleep(3)
driver.close()