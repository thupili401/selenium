import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
button=driver.find_element(By.XPATH,"//button[.='Check this']")
driver.execute_script("arguments[0].scrollIntoView(true)",button)
button.click()
wait=WebDriverWait(driver,15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='dte']"))).click()
time.sleep(3)