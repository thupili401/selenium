import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(By.XPATH,"//button[.='Dropdown']").click()
wait=WebDriverWait(driver,30)
flipkart=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[.='Flipkart']")))
flipkart.click()
time.sleep(3)
driver.close()