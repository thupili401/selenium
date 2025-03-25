import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
parent_window=driver.current_window_handle
driver.find_element(By.XPATH,"//a[.='Open a popup window']").click()
windows=driver.window_handles

for i in windows:
    driver.switch_to.window(i)
    if driver.title.__eq__("New Window"):
        Para=driver.find_element(By.XPATH,"//h3[.='New Window']").text
        print(Para)
        driver.close()
        break
driver.switch_to.window(parent_window)
driver.find_element(By.ID,"ta1").send_keys("Sreekanth")
time.sleep(3)
driver.quit()