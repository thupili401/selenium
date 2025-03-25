from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://getbootstrap.com/docs/4.0/components/dropdowns/")
driver.find_element(By.XPATH,"//button[@id='dropdownMenuButton']").click()
#driver.find_element(By.XPATH,"//button[@id='dropdownMenuButton']/following-sibling::div/a[1]").click()
a=driver.find_elements(By.XPATH,"//button[@id='dropdownMenuButton']/following-sibling::div")
for i in a:
    print(i.text)
     
driver.close()