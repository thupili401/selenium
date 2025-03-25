import time

from selenium  import webdriver
from selenium.webdriver.common.by import By
Chrome_Options=webdriver.ChromeOptions()
Chrome_Options.add_argument("--start-maximized")
driver=webdriver.Chrome(options=Chrome_Options)
time.sleep(3)
driver.quit()