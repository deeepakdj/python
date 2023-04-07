import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "pwd").send_keys("manager")
driver.find_element(By.XPATH, "//div[.='Login ']").click()
driver.find_element(By.ID, "container_tasks").click()
driver.find_element(By.XPATH, "//div[.='Add New']").click()
driver.find_element(By.XPATH, "//div[.='+ New Customer']").click()
driver.find_element(By.XPATH, "//div[@class='customerNameDiv']/input[@placeholder='Enter Customer Name']")\
    .send_keys("BUR DEEP")
driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Customer Description']").send_keys("Hdfc")
driver.find_element(By.XPATH, "//div[text()='- Select Customer -']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='searchItemList']/div[.='Galaxy Corporation']").click()
driver.find_element(By.XPATH, "//div[@class='components_button withPlusIcon']").click()
time.sleep(10)
driver.find_element(By.LINK_TEXT, 'Logout').click()
