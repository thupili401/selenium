import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

def test_redbus():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.redbus.in/")
    allure.attach(driver.get_screenshot_as_png(), name='test_redbus', attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()

@allure.severity(allure.severity_level.BLOCKER)
def test_redbus():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.redbus.in/")
    allure.attach(driver.get_screenshot_as_png(), name='test_redbus', attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()

@allure.severity(allure.severity_level.CRITICAL)
def test_Abhibus():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.abhibus.com/")
    allure.attach(driver.get_screenshot_as_png(), name='test_Abhibus', attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()
@allure.severity(allure.severity_level.MINOR)
def test_yatra():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    allure.attach(driver.get_screenshot_as_png(), name='test_yatra', attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()
@allure.severity(allure.severity_level.NORMAL)
def test_Makemytrip():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")
    allure.attach(driver.get_screenshot_as_png(), name='test_Makemytrip', attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()