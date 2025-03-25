from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
text_retrive=driver.find_element(By.XPATH,"//p[text()='PracticeAutomationHere']").text
# text command can be used wgent the text is between tags#
print(text_retrive)
driver.title
driver.close()