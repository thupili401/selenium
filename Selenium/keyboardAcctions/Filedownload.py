import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def Chrome_Setup():
    #To download file for desired location
    preferences={"download.default_directory":location}
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver
def Edge_Setup():
    #To download file for desired location
    preferences={"download.default_directory":location}
    edge_options=webdriver.EdgeOptions()
    edge_options.add_experimental_option("prefs",preferences)
    driver=webdriver.Edge(options=edge_options)
    driver.implicitly_wait(10)
    return driver

driver=Chrome_Setup()
driver=Edge_Setup()
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='download/selenide-intro.txt']").click()
time.sleep(5)




