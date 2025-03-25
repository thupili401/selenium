import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source=driver.find_element(By.XPATH,"//div[@id='box6']")
destination=driver.find_element(By.XPATH,"//div[@id='box106']")
actions=ActionChains(driver)
actions.click_and_hold(source).move_to_element(destination).release().perform()
#actions.drag_and_drop(source,destination).perform()
time.sleep(3)
driver.quit()