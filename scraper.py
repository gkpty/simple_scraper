from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import os

url = "https://www.encuentra24.com/panama-es/anuncios-casificados-miscelaneos-vende-ropa"
#get the driver path
driver = webdriver.Chrome(executable_path="/home/fargo/Downloads/chromedriver")
#open browser window
driver.get(url)

pests = driver.find_elements_by_class_name("ann-box-title")
size = len(pests)

i=0
while i < size:
	posts = driver.find_elements_by_class_name("ann-box-title")
	posts[i].click()
	i += 1
	soup = BeautifulSoup(driver.page_source, "html.parser")
	for name in soup.findAll(attrs={'class' : 'user-name'}):
		x = name.text
		break
	for phone in soup.findAll(attrs={'class' : 'phone-confirmed'}):
		a = phone.text
		b = a.split('V')
		c = b[0]
		break
	print(x, c)
	driver.back()
	i += 1
	continue
