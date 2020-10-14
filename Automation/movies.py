from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\Sri\Downloads\chromedriver')
driver.get('http://103.133.204.82/Data/Disk2/English%20Movie/')
links = driver.find_element_by_xpath('/html/body/pre')
print(links.text)
