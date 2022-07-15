# Download visual studio - https://code.visualstudio.com/download
# pip install selenium
# pip install pandas
# pip install pynput
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key, Controller
import pandas as pd

df = pd.read_csv('rc_list.csv')

for index, row in df.iterrows():
    path = 'C:\Program Files (x86)\msedgedriver.exe' # go to https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ to download this
    driver = webdriver.Edge(path)
    driver.get('https://vahan.parivahan.gov.in/nrservices/faces/user/citizen/searchstatus.xhtml')

    mobileField = driver.find_element_by_name("TfMOBILENO")
    mobileField.send_keys("number")
    mobileField.send_keys(Keys.RETURN)

    # time.sleep(1)

    passwordField = driver.find_element_by_name("tfPASSWORD")
    passwordField.send_keys("password")
    passwordField.send_keys(Keys.RETURN)

    # time.sleep(1)

    rcField = driver.find_element_by_id("regn_no1_exact")
    rcField.send_keys(row)

    time_pass = input("Press enter when ready: ")
    print(time_pass)

    time.sleep(1)
    

    keyboard = Controller()
    keyboard.press(Key.ctrl)
    time.sleep(0.2)
    keyboard.press('p')
    time.sleep(0.2)
    keyboard.release('p')
    time.sleep(0.2)
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

    time.sleep(1)

    driver.quit()