import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.worldometers.info/geography/flags-of-the-world/')
#1.scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# time.sleep(5)
# print("Number of pixel value",value)

#scroll till finding the element
# flag=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div/div/div[79]/div/a/img")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
#  value=driver.execute_script("return window.pageYOffset;")
#  print("Number of pixel value",value)
# time.sleep(5)

#scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixel value",value)
time.sleep(5)

#scroll upto starting point
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixel value",value)
time.sleep(5)
driver.close()