# 
# Download visual studio - https://code.visualstudio.com/download
# pip install selenium
# pip install pandas
# pip install pynput
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from PIL import Image
from io import BytesIO

from sqlalchemy import true

df = pd.read_csv('rc_list.csv')
batch_num = 0

for index, row in df.iterrows():
    
    row = str(row)
    row = row.split(" ")
    splitted_list = row[4]
    splitted_list = splitted_list.split("\nName:")

    reg_num = splitted_list[0]
    
    path = 'C:\Program Files (x86)\msedgedriver.exe' # go to https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ to download this
    driver = webdriver.Edge(path)
    driver.get('https://vahan.parivahan.gov.in/nrservices/faces/user/citizen/searchstatus.xhtml')

    mobileField = driver.find_element_by_name("TfMOBILENO")
    mobileField.send_keys("number")
    mobileField.send_keys(Keys.RETURN)

    passwordField = driver.find_element_by_name("tfPASSWORD")
    passwordField.send_keys("password")
    passwordField.send_keys(Keys.RETURN)

    rcField = driver.find_element_by_id("regn_no1_exact")
    rcField.send_keys(reg_num)

    current_url = driver.current_url

    while true:
        if current_url == "https://vahan.parivahan.gov.in/nrservices/faces/user/citizen/searchVehicleDetails.xhtml":
            break
        else:
            current_url = driver.current_url

    time.sleep(0.1)

    if index%50 == 0:
        batch_num = batch_num+1

    img = Image.open(BytesIO(driver.find_element_by_tag_name('body').screenshot_as_png)).convert('RGB')
    img.save(f'{batch_num}_{index+1}_{reg_num}.pdf', "PDF", quality=100)

    time.sleep(0.2)

    driver.quit()