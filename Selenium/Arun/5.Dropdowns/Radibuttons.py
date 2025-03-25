import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
i=driver.find_element(By.ID,"radio1")
if i.is_selected():
    pass
else:
    i.click()
time.sleep(3)
driver.close()
