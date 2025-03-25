import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
Chrome_options=Options()
Chrome_options.add_experimental_option("excludeSwitches",["enable_automation"])
Chrome_options.add_experimental_option("useAutomationExtension",False)
Chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver=webdriver.Chrome(options=Chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/")
print(driver.title)
time.sleep(5)
driver.close()