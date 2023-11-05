import time
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
a = driver.find_element(By.ID, value="radio1")

print(a.is_selected())

if a.is_selected():
    print("Not Selected")
    pass
else:
    a.click()
    print("Selected")

