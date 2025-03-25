import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://omayo.blogspot.com/')
dropdown_list=driver.find_element(By.XPATH,"//select[@id='drop1']")
dropdown=Select(dropdown_list)
#dropdown.select_by_visible_text('doc 1')
#dropdown.select_by_value('jkl')
#dropdown.select_by_index(3) #index


##capture all the options and print them
alloptions=dropdown.options
print("Total number of options is: ",len(alloptions))

for i in alloptions:
    print(i.text)


###select option from dropdown with out using built in method

for i in alloptions:
    if i.text=='doc 4':
        i.click()
        break
time.sleep(3)
driver.close()

