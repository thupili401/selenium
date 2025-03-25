import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
button=driver.find_element(By.XPATH,"//button[.='Dropdown']")
driver.execute_script("arguments[0].scrollIntoView(true);",button)
button.click()
wait=WebDriverWait(driver,10)
drop_down=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[.='Facebook']")))
drop_down.click()
time.sleep(3)
driver.close()
