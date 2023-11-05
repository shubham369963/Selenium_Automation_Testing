import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in/umesh/Upload%20and%20Download.html")
act = ActionChains(driver)
driver.maximize_window()

# scrolldown
driver.execute_script("window.scrollBy(0,500)", "")

# download
menu = driver.find_element(By.XPATH, value='//*[@id="downloadButton"]')
act.click(menu).perform()
# upload
fl = driver.find_element(By.XPATH, value='//*[@id="uploadFile"]')
fl.send_keys("C:\\Users\\Lenovo\\Downloads\\sampleFile.jpeg")
