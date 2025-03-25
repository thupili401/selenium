import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_actions=webdriver.ChromeOptions()
Chrome_actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("9912866236")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("lee.ece.01")
time.sleep(5)
driver.close()