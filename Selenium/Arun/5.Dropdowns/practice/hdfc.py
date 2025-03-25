from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.hdfcbank.com/")
driver.find_element(By.XPATH,"//a[contains(text(),'Select Product Type')]").click()
a=driver.find_elements(By.XPATH,"//a[contains(text(),'Select Product Type')]/following-sibling::ul")

for i in a:
    print(i.text)