import time
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://codify-app.onrender.com/login")
driver.maximize_window()

#id takne
driver.find_element(By.XPATH, value="/html/body/div/main/div/div/div/div/div/form/div[1]/input").send_keys("shubhamhalade1712@gmail.com")

#pass takne
driver.find_element(By.XPATH, value="//*[@id='formBasicPassword']").send_keys("123")

#btn tap karne
driver.find_element(By.CLASS_NAME, value="mt-4.btn.btn-primary").click()

# for practice refer  https://omayo.blogspot.com/