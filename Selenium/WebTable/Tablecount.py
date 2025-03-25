from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome(Chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
Rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
Columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(Rows))
print(len(Columns))
##to select specific row##
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[2]").text
print(data)