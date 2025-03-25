from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_Actions=webdriver.ChromeOptions()
Chrome_Actions.add_argument('--disable-notifications')
driver=webdriver.Chrome(options=Chrome_Actions)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

##Self
# data=driver.find_element(By.XPATH,"//a[contains(text(),'LT Foods Ltd.')]/self::ta").text
# print(data)

##parent
# data=driver.find_element(By.XPATH,"//a[contains(text(),'LT Foods Ltd.')]/parent::td").text
# print(data)

#child
# child=driver.find_elements(By.XPATH,"//a[contains(text(),'LT Foods Ltd.')]/ancestor::tr/child::td")
# print(len(child))
# for i in child:
#     print(i.text)
##ancestor
child=driver.find_element(By.XPATH,"//a[contains(text(),'LT Foods Ltd.')]/ancestor::tr").text
print(child)