import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
driver.save_screenshot("a.png")
button=driver.find_element(By.XPATH,"//span[@class='input-group-btn']")
button.screenshot("c.png")
a=driver.find_element(By.XPATH,"//input[@class='form-control input-lg']")
a.click()
a.send_keys("moniter")
driver.find_element(By.XPATH,"//span[@class='input-group-btn']").click()
driver.save_screenshot("b.png")
time.sleep(3)