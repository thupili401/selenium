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
wait=WebDriverWait(driver,10)
cal=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='flatpickr-innerContainer']")))
driver.find_element(By.CLASS_NAME,"arrowUp").click()
current_month=driver.find_element(By.CLASS_NAME,"cur-month").text.strip()
while not(current_month=="November"):
  driver.find_element(By.CLASS_NAME,"flatpickr-next-month").click()
  current_month = driver.find_element(By.CLASS_NAME, "cur-month").text
  time.sleep(3)

driver.find_element(By.XPATH,"//span[@aria-label='December 19, 2025']").click()
time.sleep(3)
driver.quit()

