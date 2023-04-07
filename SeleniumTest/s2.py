import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')
driver.find_element('name','q').send_keys('linkedin login')
time.sleep(3)
driver.find_element('name','q').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,'LinkedIn Login').click()
time.sleep(3)
driver.find_element('id','username').send_keys('deeepakdj007@gmail.com')
driver.find_element(By.ID,'password').send_keys('deepak26*')
driver.find_element('xpath',"//button[@type='submit']").click()
time.sleep(3)
print('working Successfully')