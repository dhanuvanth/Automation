from selenium import webdriver
from time import sleep
import pytesseract
from PIL import Image
import urllib.request
from cv2 import cv2
from captcha import img_txt


def automation(link):
    driver = webdriver.Chrome(
        r'C:\Users\Dhanu\Downloads\chromedriver.exe')  # check this path
    driver.maximize_window()
    driver.get(link)
    sleep(2)
    keywords = driver.find_element_by_xpath('//*[@id="skeyword"]')
    keywords.send_keys('building')
    img_link = driver.find_element_by_xpath(
        '//*[@id="latestactivetendersnew-form"]/div[2]/div/div[8]/div/img').get_attribute("src")
    urllib.request.urlretrieve(img_link, 'captcha.png')
    # To convert captcha into txt
    # img = cv2.imread('captcha.png', 0)
    # blur = cv2.GaussianBlur(img, (5, 5), 0)
    # ret, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # cv2.imwrite('captcha.png', th3)
    # txt = pytesseract.image_to_string(Image.open('captcha.png'), lang="eng")
    # print(txt.strip())

    # To convert captcha into txt using module
    imgTxt = img_txt('captcha.png')
    txt = imgTxt.txt()
    sleep(2)

    captcha = driver.find_element_by_xpath('//*[@id="edit-captcha-response"]')
    captcha.send_keys(txt)
    sleep(2)

    search = driver.find_element_by_xpath('//*[@id="btnSearch"]')
    search.click()
    sleep(2)

    driver.execute_script('window.scrollTo(0,400)')
    link_1 = driver.find_element_by_xpath(
        '//*[@id="table"]/tbody/tr[1]/td[5]/a')
    link_1.click()
    sleep(2)

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    link_2 = driver.find_element_by_xpath('//*[@id="tenderDetailDivTd"]/div/a')
    link_2.click()
    sleep(2)

    prnt = driver.find_element_by_xpath('//*[@id="DirectLink"]')
    prnt.click()
    print('print is cicked')
    sleep(200)


url_cpp = 'https://eprocure.gov.in/cppp/latestactivetendersnew/cpppdata'
url_mmp = 'https://eprocure.gov.in/cppp/latestactivetendersnew/mmpdata'
automation(url_cpp)
