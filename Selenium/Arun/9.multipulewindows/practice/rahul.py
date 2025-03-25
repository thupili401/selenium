import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
parent_window = driver.current_window_handle
driver.find_element(By.ID, 'openwindow').click()
windows = driver.window_handles
for i in windows:
    driver.switch_to.window(i)
    if driver.current_url.__eq__("https://www.qaclickacademy.com/"):
        driver.find_element(By.XPATH, "(//a[.='Courses'])[1]").click()
        driver.close()

driver.switch_to.window(parent_window)
driver.find_element(By.ID, "opentab").click()
time.sleep(3)
driver.close()

time.sleep(3)
