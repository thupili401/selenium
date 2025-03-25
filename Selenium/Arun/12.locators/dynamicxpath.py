import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
for i in range(1,6):
    xpath_text= "//div[@id='LinkList1']/child::div/ul/li["+str(i)+"]"
    time.sleep(3)
    wait = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,xpath_text)))
    wait.click()
    time.sleep(3)
    driver.back()
driver.close()
