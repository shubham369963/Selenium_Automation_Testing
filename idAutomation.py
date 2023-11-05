from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Launch browser
driver=webdriver.Firefox()

#Enter ULR
driver.get("https://codify-app.onrender.com/login")

#id takne
driver.find_element(By.ID, value="formBasicEmail").send_keys("shubhamhalade1712@gmail.com")

#pass takne
driver.find_element(By.ID, value="formBasicPassword").send_keys("123")

#btn tap karne
driver.find_element(By.CLASS_NAME, value="mt-4.btn.btn-primary").click()