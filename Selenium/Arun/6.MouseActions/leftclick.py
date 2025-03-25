import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
actions=ActionChains(driver)
blog=driver.find_element(By.XPATH,"//a[@value='link1']")
actions.click(blog).perform()
time.sleep(3)
driver.close()