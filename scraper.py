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
z = 0

while z< 10:
	pests = driver.find_elements_by_class_name("ann-box-title")
	i = 0
	for pest in pests:
		posts = driver.find_elements_by_class_name("ann-box-title")
		posts[i].click()
		i += 1
		item_category = driver.find_element_by_xpath("""/html/body/section[3]/div[4]/div/div/div/ul/li[1]/span[2]""").text
		pub_date = driver.find_element_by_xpath("""/html/body/section[3]/div[4]/div/div/div/ul/li[2]/span[2]""").text
		h = driver.find_element_by_class_name("product-title").text
		j = h.split('| ')
		item_title = j[1]
		item_location = driver.find_element_by_xpath("""/html/body/section[3]/div[4]/div/div/div/ul/li[3]/span[2]""").text
		item_price = driver.find_element_by_xpath("""/html/body/section[3]/div[4]/div/div/div/ul/li[4]/span[2]""").text
		a = driver.find_element_by_xpath("""//*[@id="contactBox"]/div/div[2]/div/div[1]/div[2]/span[1]""").text
		b = a.split('V')
		owner_phone = b[0]
		owner_name = driver.find_element_by_xpath("""//*[@id="contactBox"]/div/div[2]/div/div[1]/div[1]/span[2]""").text
		x = driver.find_element_by_class_name("ad-id").text
		y = x.split(':')
		post_id = y[1]
		print(owner_name, owner_phone, post_id, item_title, item_category, pub_date, item_location, item_price)
		driver.back()
		i += 1
	nextpage = driver.find_element_by_xpath("""//*[@id="listingview"]/div[2]/div[2]/nav/ul/li[7]/a""")
	nextpage.click()
