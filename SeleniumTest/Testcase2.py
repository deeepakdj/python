import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.yahoo.com/")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("adamgowda@yahoo.com")
driver.find_element(By.ID, "login-signin").click()
driver.find_element(By.ID, "login-passwd").send_keys("Yahoo@1234")
driver.find_element(By.ID, "login-signin").click()
driver.find_element(By.ID, "ybarMailLink").click()
driver.find_element(By.LINK_TEXT, "Compose").click()
time.sleep(10)
