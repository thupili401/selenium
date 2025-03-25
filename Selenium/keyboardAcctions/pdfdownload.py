import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location =os.getcwd()

def Chrome_Browser():
    preferences = {"download.default_directory": location,"plugins.always_open_pdf_externally":True}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
time.sleep(5)
driver.find_element(By.XPATH,"//a[@href='https://file-examples.com/wp-content/storage/2017/10/file-sample_150kB.pdf']").click()
time.sleep(5)