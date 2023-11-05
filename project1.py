# print("hello")
# a = int(input("Enter Value: "))
# print(type(a))

# logical = || , &&,  !
# arithmetic = + , -, *, /, %, **
# relational = >, <, >=, <=, ==
# assignment = =, +=, *=, -=, /=
# increment = ++, --
# special
# bitwise
# conditional
# LARA IS BC

# list=[10,10,True, "Nice"]
# print(type(list))
# print(list)


# a =10
# if a>=0:
#     print("number is positive")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() #creating driver for firefox browser
driver.get("https://upcode-app.onrender.com/") #launch browser url
driver.minimize_window() #minimize window of browser

print(driver.title) #printing title of website

