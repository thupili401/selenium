from selenium import webdriver
from selenium.webdriver.common.by import By
browser_action=webdriver.ChromeOptions()
browser_action.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=browser_action)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
actions=driver.switch_to.alert
print(actions.text)
actions.accept()
