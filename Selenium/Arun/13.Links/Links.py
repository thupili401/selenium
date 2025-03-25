import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://www.embibe.com/")
links=driver.find_elements(By.TAG_NAME,'a')

broken_link_count=0
valid_link_count=0
for i in links:
    url=i.get_attribute('href')
    try:
        response=requests.get(url)
        if response.status_code>=400:
            print(f"broken link",url)
            broken_link_count+=1
        else:
            #print(f"Not broken link",url)
            valid_link_count+=1
    except requests.exceptions.RequestException as e:
        print(f"error checking {url},{e}")
        broken_link_count+=1
driver.close()
print("Total links is",len(links))
print("Total Broken link is :",broken_link_count)
print("Total valid links is : ",valid_link_count)