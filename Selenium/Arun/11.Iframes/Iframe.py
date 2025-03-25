import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_actions=webdriver.ChromeOptions()
Chrome_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='tinymce']").clear()
time.sleep(3)
