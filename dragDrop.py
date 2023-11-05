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
act = ActionChains(driver)
driver.maximize_window()

# scrolldown
driver.execute_script("window.scrollBy(0,600)", "")

source = driver.find_element(By.XPATH, value='//*[@id="draggable"]')
target = driver.find_element(By.XPATH, value='//*[@id="droppable"]')

act.drag_and_drop(source,target).perform()

