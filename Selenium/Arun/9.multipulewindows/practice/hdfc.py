import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.hdfcbank.com/")
parent= driver.current_window_handle
driver.find_element(By.XPATH,"//button[.='Login' and @ng-mouseover]").click()
driver.find_element(By.XPATH,"//a[@target='_blank' and .='NetBanking']").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
y=driver.find_element(By.XPATH,"//frame[@marginheight='0']")
driver.switch_to.frame(y)
driver.find_element(By.XPATH,"//input[@class='form-control text-muted']").send_keys("thupili")
time.sleep(3)
driver.find_element(By.XPATH,"//a[.='CONTINUE']").click()
time.sleep(5)
driver.close()
time.sleep(3)
driver.switch_to.window(parent)
driver.find_element(By.XPATH,"//li[@class='active']/following-sibling::li[1]/a").click()
time.sleep(3)
driver.close()