from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://testpages.eviltester.com/styled/basic-web-page-test.html")
Html=driver.page_source
print(Html)