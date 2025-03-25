from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_actions=webdriver.ChromeOptions()
Chrome_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(Chrome_actions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
Rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
Columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")

for r in range(2,len(Rows)+1):
    author_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if author_name=="Mukesh":
        Book_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        prize = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        print(Book_name,author_name,prize)
driver.close()