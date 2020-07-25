from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from process_names_dates import process_author_date
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidArgumentException

def scrape_page(url_to_parse):

   chrome_options = Options()     
   chrome_options.add_argument('--headless')     
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('start-maximized')     
   chrome_options.add_argument('disable-infobars')     
   chrome_options.add_argument("--disable-extensions") 
   driver = webdriver.Chrome(options=chrome_options)

   news_url = url_to_parse
   try:
      driver.get(news_url)
   except InvalidArgumentException:
      print('invalid arg here: ' + str(news_url))
   show_comments_xpath = "//*[contains(text(), 'Показать комментарии ')]"

   # show_comments_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, show_comments_xpath)))
   show_comments_button = driver.find_element_by_xpath(show_comments_xpath)
   driver.execute_script("arguments[0].click();", show_comments_button)

   show_all_comments_xpath = "//*[contains(text(), 'Посмотреть все')]"
   try:
      show_all_comments_button = driver.find_element_by_xpath(show_all_comments_xpath)
      driver.execute_script("arguments[0].click();", show_all_comments_button)

   except NoSuchElementException:
      print('malo comentov...!')
      
   # show_all_comments_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, show_all_comments_xpath)))


   list_of_comments = driver.find_elements_by_class_name('tn-comment-item')
   # print('-------------------------length of list of coments: %d' % len(list_of_comments))
   collected_author_date = list()

   comments_text = list()
   for comment in list_of_comments:
      user_date_likes_element = comment.find_element_by_class_name('tn-comment-item-content-metadata')
      collected_author_date.append(user_date_likes_element.text.split(' '))
      commment_text_element = comment.find_element_by_class_name('tn-comment-item-content-text')
      comments_text.append(commment_text_element.text)

   driver.quit()#close the browser here
   collected_author_date = list(filter(lambda l: len(l)> 1, collected_author_date))
   # print('---------------------------------------------')
   
   additional_format_dates(collected_author_date)
   # for c in collected_author_date:
   #    print(c)


   collected_author_date = process_author_date(collected_author_date)

   general_data = [list(a) for a in zip(collected_author_date, comments_text)]
   general_data = [[*author_name, comment_text] for author_name,comment_text in general_data]

   if len(general_data) > 100:
      general_data = general_data[:100]
   # for x in general_data:
   #    print(x)
   return general_data


href = 'https://tengrinews.kz/kazakhstan_news/ajiotaj-vokrug-novogo-chudo-sredstva-koronavirusa-voznik-409051/'

# scrape_page(href)

def additional_format_dates(collected_author_date):
   for item in collected_author_date:
      last = item[-1]
      last = last.split('\n')
      if len(last) > 1:
         item[-1] = last[0]
   