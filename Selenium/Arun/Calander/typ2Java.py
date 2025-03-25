import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.path2usa.com/travel-companion/")
time.sleep(5)
driver.find_element(By.ID,"form-field-travel_comp_date").click()
driver.execute_script("document.getElementById('form-field-travel_comp_date').value='25/12/2026'")
time.sleep(5)
driver.quit()

