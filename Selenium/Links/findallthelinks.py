from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/digital-downloads')
links=driver.find_elements(By.TAG_NAME,'a')#to  get all the links in webpage
#links=driver.find_elements(By.XPATH,"//a") #to  get all the links in webpage

print("Number of links is : ",len(links))

for i in links: ###to print all the links
     print(i.text)

driver.quit()
