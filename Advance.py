import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# driver.find_element(By.XPATH, value="//*[@id='HTML4']/div[1]/button").click()

# scrolldown
driver.execute_script(script="window.scrollBy(0,800)", args="")

'''
driver.find_element(By.XPATH, value="//*[@id='HTML9']/div[1]/button[1]").click()
ab = driver.switch_to.alert
time.sleep(5)
ab.accept()
'''




