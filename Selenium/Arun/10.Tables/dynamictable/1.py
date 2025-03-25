import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.opencart.com/admin/index.php?route=common/dashboard&user_token=31dd374ed3ce99de502251647e0501f7")
driver.find_element(By.ID,"input-username").send_keys('demo')
driver.find_element(By.ID,"input-password").send_keys('demo')
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
time.sleep(5)