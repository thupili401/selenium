import time

from selenium  import webdriver
from selenium.webdriver.common.by import By
Chrome_Options=webdriver.ChromeOptions()
Chrome_Options.add_argument("--kiosk")
driver=webdriver.Chrome(options=Chrome_Options)
#driver.fullscreen_window()
time.sleep(3)
driver.quit()