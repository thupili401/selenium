import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.set_window_size(300,800)
time.sleep(5)
driver.fullscreen_window()
time.sleep(5)
driver.close()