import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
actions=ActionChains(driver)
blog=driver.find_element(By.XPATH,"//span[.='Home & Furniture']")
actions.move_to_element(blog).perform()
time.sleep(1)
driver.find_element(By.XPATH,"//a[.='Bedroom Furniture']").click()
time.sleep(5)
driver.quit()