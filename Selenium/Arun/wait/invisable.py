import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(By.XPATH,"//button[.='Start']").click()
wait=WebDriverWait(driver,30)
invisable=wait.until(expected_conditions.invisibility_of_element((By.XPATH,"//div[@id='loading']")))
a=driver.find_element(By.XPATH,"//h4[.='Hello World!']").text
print(a)
time.sleep(3)