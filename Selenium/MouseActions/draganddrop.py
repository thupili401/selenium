import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
Browser_Actions=webdriver.ChromeOptions()
Browser_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Browser_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(3)
source=driver.find_element(By.XPATH,"//div[@id='box6']")
destination=driver.find_element(By.XPATH,"//div[@id='box106']")
act=ActionChains(driver)
act.drag_and_drop(source,destination).perform()
time.sleep(5)