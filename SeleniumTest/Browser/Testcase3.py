import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/maps")
driver.find_element(By.ID, "searchboxinput").send_keys("Mysore")
driver.find_element(By.ID, "hArJGc").click()
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Choose starting point')]").send_keys("Bangalore")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Choose starting point')]").send_keys(Keys.ENTER)
time.sleep(10)
text = driver.find_element(By.ID, "section-directions-trip-0").screenshot_as_png
print(text)
