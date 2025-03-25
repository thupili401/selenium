from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.find_element(By.XPATH,"//input[@id='justAnInputBox']").click()
