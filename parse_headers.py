from selenium import webdriver
import datetime as dt
from datetime import datetime as dd
from selenium.webdriver.chrome.options import Options
from process_news_dates import process_news_dates
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()     
chrome_options.add_argument('--headless')     
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('start-maximized') 
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('disable-infobars')  
# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-extensions") 


# HEADERS---------------------------------------------------------------------------------------
def get_headers():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://tengrinews.kz")   
    news_headers_element = driver.find_elements_by_xpath('(.//span[@class = "tn-main-news-title"])')
    news_headers = list()
    for head in news_headers_element:
        news_headers.append(head.text) 

    driver.quit()
    return news_headers

