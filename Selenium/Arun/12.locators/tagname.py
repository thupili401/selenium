from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.automationpractice.pl/index.php")
slider=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(slider))
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
for i in links:
    print(i.get_attribute("href"))