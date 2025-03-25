import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.execute_script("document.getElementById('datepicker').value='25/12/2026'")
time.sleep(3)
driver.close()