from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('chromedriver.exe') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = 'sri bro'
  
# Replace the below string with your own message 
string = "Message sent using Python!!!"
  
x_arg = '//*[@id="side"]/div[1]/div/label/div/div[2]'
Name = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
Name.send_keys(target + Keys.ENTER)

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath))) 
for i in range(5): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1) 