from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import os
import datetime

start = datetime.date.today()
end = datetime.date(2020,10,6)

df = pd.read_excel(os.getcwd() + '\\Website Ranking Works.xlsx',sheet_name='Automation Update')
arr = df.values

for i in range(len(arr[:,0])):

    if(start >= end):
        driver = webdriver.Chrome(os.getcwd() + '\\chromedriver.exe')  # check this path
    driver.maximize_window()
    driver.get('https://www.usalistingdirectory.com/submit.php')
    wait = WebDriverWait(driver, 600) 

    link = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')))
    link.click()

    title = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input')))
    # title = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input')
    title.send_keys('Corporate Training')

    url = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')))
    # url = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input')
    url.send_keys('https://www.mazenetsolution.com/corporate-training/')

    desc = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/textarea')))
    # desc = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/textarea')
    desc.send_keys('Corporate Training - - Mazenet is a workforce development organization in Information Technology benefiting many corporates across different geographies')

    keyword = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input')))
    # keyword = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input')
    keyword.send_keys('Corporate Training')

    desc_meta = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[7]/td[2]/textarea')))
    # desc_meta = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[7]/td[2]/textarea')
    desc_meta.send_keys('Corporate Training - - Mazenet is a workforce development organization in Information Technology benefiting many corporates across different geographies')

    name = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[8]/td[2]/input')))
    # name = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[8]/td[2]/input')
    name.send_keys('Mazenet Solution')

    email = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[9]/td[2]/input')))
    # email = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[9]/td[2]/input')
    email.send_keys('mazenetsubmission@gmail.com')

    catageries = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[10]/td[2]/select/option[54]')))
    # catageries = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[10]/td[2]/select/option[54]')
    catageries.click()

    agree = wait.until(EC.presence_of_element_located(( By.XPATH,'//*[@id="AGREERULES"]')))
    # agree = driver.find_element_by_xpath('//*[@id="AGREERULES"]')
    agree.click()

    submit = wait.until(EC.presence_of_element_located(( By.XPATH,'/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[13]/td/input')))
    # submit = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/form/table/tbody/tr[13]/td/input')
    submit.click()

    driver.close()