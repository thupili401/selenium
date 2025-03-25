import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/")
blog=driver.find_element(By.NAME,"search")
actions=ActionChains(driver)
actions.context_click(blog).perform()
time.sleep(3)
driver.quit()