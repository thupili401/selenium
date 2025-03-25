import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
blog=driver.find_element(By.XPATH,"//p[.='Double-click']")
actions=ActionChains(driver)
actions.double_click(blog).perform()
time.sleep(3)
driver.quit()