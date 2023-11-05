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

chk_bx = driver.find_element(By.ID, value="checkbox1")

if chk_bx.is_selected():
    pass
else:
    chk_bx.click()

chk_bx1 = driver.find_element(By.ID, value="checkbox2")
chk_bx1.click()

time.sleep(5)
if chk_bx.is_selected() and chk_bx1.is_selected():
    chk_bx.click()
    time.sleep(5)
    chk_bx1.click()

