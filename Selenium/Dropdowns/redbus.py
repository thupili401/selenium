import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")
a=driver.find_element(By.ID,"src")
a.clear()
a.send_keys("Ne")
time.sleep(3)
actions=ActionChains(driver)
actions.move_to_element(a).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
time.sleep(5)
driver.quit()