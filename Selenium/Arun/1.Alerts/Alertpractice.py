import time

from selenium import    webdriver
from selenium.webdriver.common.by import By
chrome_actions=webdriver.ChromeOptions()
chrome_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=chrome_actions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
time.sleep(5)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()