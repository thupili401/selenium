import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.find_element(By.ID,"input-email").send_keys("amotooricap9@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("12345")
obj=ActionChains(driver)
obj.send_keys(Keys.ENTER).perform()  #here we can use Keys.Return also or simply we can use submit also
time.sleep(3)
driver .quit()