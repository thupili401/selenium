import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#id=driver.current_window_handle #to get wendow id for current window bbut it wont work for multiple window
#print(id)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Privacy Policy']").click()
ids=driver.window_handles
driver.switch_to.window(ids[1])
privacy_policy_link = driver.find_element(By.XPATH, "/html/body/footer/section/div[2]/div/div/div[2]/div/ul/li[1]/a")
# Scroll the "Privacy Policy" link into view using JavaScript
driver.execute_script("arguments[0].scrollIntoView();", privacy_policy_link)

privacy_policy_link.click()
ids1 = driver.window_handles
driver.switch_to.window(ids[1])
#Approch1
#parentwindow=ids[0]
#childwindow=ids[1]
#print(parentwindow)
#driver.switch_to.window(parentwindow)
#print(driver.title)
#print(childwindow)
#driver.switch_to.window(childwindow)
#print(driver.title)
#####Approch2
# for i in ids:
#     driver.switch_to.window(i)
#     print(driver.title)
# driver.close()
time.sleep(3)
for i in ids:
    driver.switch_to.window(i)
    if driver.title=="OrangeHRM" :
        driver.close()

driver.close()