import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
product_url = ('https://smile.amazon.com/All-new-kindle-paperwhite/dp/B08N38WQSH/ref=sr_1_1_sspa?keywords=kindle+'
               'paperwhite+2022&qid=1652964961&sprefix=kindle+pa,aps,105&sr=8-1-spons&psc=1')

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
driver.get(product_url)
# http_proxy  = "http://10.10.1.10:3128"
# https_proxy = "https://10.10.1.11:1080"
# ftp_proxy   = "ftp://10.10.1.10:3128"
#
# proxyDict = {
#               "http"  : http_proxy,
#               "https" : https_proxy,
#               "ftp"   : ftp_proxy
#             }

page = requests.get(product_url, headers=header)
soup = bs(page.content, 'html.parser')
title = soup.find(id="productTitle")
#print(soup.prettify())
print(title)


driver.find_element(By.CSS_SELECTOR,".apexPriceToPay > span:nth-child(1)")
# price_element = driver.find_element(by=By.CSS_SELECTOR, value=".apexPriceToPay > span:nth-child(1)")
# useless_price_string =driver.find_element_by_css_selector(".apexPriceToPay > span:nth-child(1)")
print(f'P_element: {price_element}\nUseless= {useless_price_string}')

#price = useless_price_string.lstrip('$')

#print(f'Title = {title}\nPrice = {price}, ')
