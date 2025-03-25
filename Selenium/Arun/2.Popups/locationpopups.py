
from selenium import webdriver
Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.homedepot.com/")