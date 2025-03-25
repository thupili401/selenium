from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.implicitly_wait(10)

for i in range(1,6):
    links="(//div[@id='LinkList1']//a)["+str(i)+"]"
    driver.find_element(By.XPATH,links).click()
    driver.back()
driver.quit()


