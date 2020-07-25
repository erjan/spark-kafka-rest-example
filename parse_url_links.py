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



# URL LINKS----------------------------------------------------------------------------------

def get_news_links():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://tengrinews.kz")

    news_links = list()
    major_news_css_selector = ".firs-column > a:nth-child(5)"

    major_news = driver.find_element_by_css_selector(major_news_css_selector).get_attribute('href')
    news_links.append(major_news)

    for i in range(2,8):
        news_l = driver.find_element_by_css_selector('div.tn-main-news-item:nth-child(' + str(i) + ') > a:nth-child(4)').get_attribute('href')
        news_links.append(news_l)

    # URL_ID
    url_ids = list()
    for url in news_links:
        u = url.split('-')[-1][:-1]
        url_ids.append(u)

    return (news_links, url_ids)

# res = get_news_links()

# for i,j in zip(res[0], res[1]):
#     print(i,j)
