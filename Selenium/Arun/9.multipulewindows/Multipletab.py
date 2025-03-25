import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
parent=driver.current_window_handle
driver.find_element(By.XPATH,"//a[.='http://www.Selenium143.blogspot.com']").click()
windows=driver.window_handles
for i in windows:
    driver.switch_to.window(i)
    if driver.title.__eq__("Selenium143"):
        driver.find_element(By.XPATH, "//a[.='What is Selenium?']").click()
        time.sleep(3)
        driver.close()
        break
driver.switch_to.window(parent)
driver.find_element(By.ID,"ta1").send_keys("Sreekanth")
time.sleep(3)
driver.quit()


