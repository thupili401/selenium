import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
parent=driver.current_window_handle
time.sleep(3)
driver.find_element(By.XPATH,"//a[.='Open a popup window']").click()
time.sleep(3)
windows=driver.window_handles
driver.switch_to.window(windows[1])
Para=driver.find_element(By.XPATH,"//h3[.='New Window']").text
time.sleep(3)
print(Para)
driver.close()
driver.switch_to.window(parent)
driver.find_element(By.ID,"ta1").send_keys("Sreekanth")
time.sleep(3)
driver.quit()