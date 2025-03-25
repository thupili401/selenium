import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/p/page3.html")
move=driver.find_element(By.XPATH,"//a[@aria-labelledby='price-min-label']")
actions=ActionChains(driver)
actions.drag_and_drop_by_offset(move,100,0).perform()
time.sleep(3)
actions.drag_and_drop_by_offset(move,-50,0).perform()
time.sleep(3)
driver.quit()