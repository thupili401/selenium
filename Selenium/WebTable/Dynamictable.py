import time

from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_actions=webdriver.ChromeOptions()
Chrome_actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(Chrome_actions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
#driver.find_element(By.LINK_TEXT,"Admin").click()
row=driver.find_elements(By.XPATH,"(//div[@class='oxd-table-cell oxd-padding-cell']/parent::*/child::div[@class='oxd-table-cell oxd-padding-cell'][2])/div")
print(len(row))

for i in range(1 , len(row)):
    value= driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(i)+"]/div/div[2]").text
    print(value)
