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


# NUMBER OF COMMENTS---------------------------------
def get_num_comments(news_and_url):
    driver = webdriver.Chrome(options=chrome_options)
    news_links = news_and_url[0]
    url_ids = news_and_url[1]
    number_comments = list()
    for i in range(len(url_ids)):
        driver.get(news_links[i])
        uid = url_ids[i]
        u = driver.find_element_by_css_selector('#comments_' + str(uid) +  ' > div:nth-child(1)').text
        u = str(u.split()[0])
        number_comments.append(u)
    driver.quit()

    for i in number_comments:
        print(i)
    
    return number_comments

