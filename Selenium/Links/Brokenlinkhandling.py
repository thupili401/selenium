##we need to install requests package by clicking on setting
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")
links=driver.find_elements(By.TAG_NAME,'a')
count=0
for i in links:
    url=i.get_attribute('href')
    try:
     response=requests.head(url)
    except:
        None
    if response.status_code>=400:
          print(url,"broken link")
          count+=1
    else:
        print(url,'Proper link')


print("total Broken links :",count)