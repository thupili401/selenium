import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/resizable/")
frame=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(frame)
actions=ActionChains(driver)
resize=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
time.sleep(3)
actions.drag_and_drop_by_offset(resize,50,105).perform()
time.sleep(3)
driver.quit()