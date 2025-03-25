from selenium import webdriver
from selenium.webdriver.common.by import By
browser_actions=webdriver.ChromeOptions()
browser_actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(browser_actions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
Rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
Columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
for i in range(2,len(Rows)+1):
    for j in range(1,len(Columns)+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(data, end='       ')
    print()
driver.close()
