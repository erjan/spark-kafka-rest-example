from selenium import webdriver
import datetime as dt
import time
from datetime import datetime as dd
from selenium.webdriver.chrome.options import Options
from scrape_page import scrape_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#MY OWN FUNCTIONS
from parse_dates import get_dates
from parse_url_links import get_news_links
from process_news_dates import process_news_dates
from parse_num_comments import get_num_comments
from parse_headers import get_headers
import warnings
warnings.filterwarnings("ignore")

chrome_options = Options()     
chrome_options.add_argument('--headless')     
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('start-maximized')     
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--log-level=3')  
# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-extensions") 


def main_parse():
    driver = webdriver.Chrome(options=chrome_options)

    #DATE & TIME ---------------------------------------------------------------------------
    print(" DATES -------------------------------------------------------------------------------")
    dates = get_dates()
    # for d in dates:
    #     print(d)

    print('URL LINKS----------------------------------------------------------------------------')
    #URL links-------------------------------
    news_and_url = get_news_links()
    news_links = news_and_url[0]
    # for n in news_and_url:
    #     print(n)

    print('NUM COMMENTS-----------------------------------------------------------')
    #NUM COMMENTS-------------------------------------
    num_comments_in_post = get_num_comments(news_and_url)
    num_comments_in_post = num_comments_in_post[:7]

    # for n in num_comments_in_post:
    #     print(n)
    print('NEWS HEADERS-----------------------------------------------------------')
    news_headers = get_headers()
    # for head in news_headers:
    #     print(head)

    main_data = list()

    print('---------DATES LENGTH-----------')
    print(len(dates))
    print('---------URL LINKS LENGTH-----------')
    print(len(news_links))
    print('---------NUM COMMENTS LENGTH-----------')
    print(len(num_comments_in_post))
    print('---------NEWS HEADERS LENGTH-----------')
    print(len(news_headers))

    driver.quit()
    for header, date_post, num_comments, news_href in zip(news_headers, dates, num_comments_in_post,news_links):
        main_data.append([header, date_post, num_comments, news_href])

    for item in main_data:
        num_com = int(item[2])
        if num_com == 0:
            main_data.remove(item)

    print('LENGTH OF main_data %d' % len(main_data))

    post_urls = list()
    for item in main_data:
        href = item[-1]
        post_urls.append(href)

    list_comments = list()
    for href in post_urls:
        comments_in_post = scrape_page(href)
        list_comments.append(comments_in_post)

    for i in range(len(main_data)):
        main_data[i].append(list_comments[i])

   
    return main_data

# data = main_parse()
# for item in data:
#     print('**************************')
#     print()
#     print(item)