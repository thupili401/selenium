from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(10)  #used to find wether page is loading in required time or not
driver.get("https://selenium143.blogspot.com/")
driver.quit()