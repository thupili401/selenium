import time
from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/search?fromCityName=Bangalore&fromCityId=122&toCityName=Nellore,%20Andhra%20Pradesh,%20India&toCityId=131&onward=06-Jun-2024&srcCountry=IND&destCountry=IND&sfcn=Bangla%20(basavakalyan)&stcn=Nellore&opId=0&busType=Any")
checkbox=driver.find_elements(By.XPATH,"//label[@class='custom-checkbox' and (contains(@for,'am') or contains(@for,'pm'))]")
print(len(checkbox))
for i in checkbox:
    title=i.get_attribute('title')
    print(title)
    i.click()
time.sleep(10)
driver.close()
######approch2#######

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# Chrome_Actions=webdriver.ChromeOptions()
# Chrome_Actions.add_argument("--disable-notifications")
# driver=webdriver.Chrome(options=Chrome_Actions)
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.redbus.in/search?fromCityName=Bangalore&fromCityId=122&toCityName=Nellore,%20Andhra%20Pradesh,%20India&toCityId=131&onward=06-Jun-2024&srcCountry=IND&destCountry=IND&sfcn=Bangla%20(basavakalyan)&stcn=Nellore&opId=0&busType=Any")
#
# checkbox = driver.find_elements(By.XPATH, "//ul[@class='dept-time at-time-filter']/li")
# print(len(checkbox))
# for i in range(1, len(checkbox)+1):
#     driver.find_element(By.XPATH, "//ul[@class='dept-time at-time-filter']/li[" + str(i) + "]/label[1]").click()
# time.sleep(5)
# driver.close()

