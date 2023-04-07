from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Python")
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
ele = driver.find_element(By.LINK_TEXT,'Forgotten password?')
ele.click()
print(type(ele))
time.sleep(15)
driver.close()
print("Sample test case successfully completed")