import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#Runs Chrome in headless mode, meaning it will not display a
# graphical interface but will still load and interact with the web page.
Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=Chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://embibe.com/")
time.sleep(3)
page_title=driver.title
print(page_title)
driver.quit()