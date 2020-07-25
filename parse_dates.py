from selenium import webdriver
import datetime as dt
from datetime import datetime as dd
from selenium.webdriver.chrome.options import Options
from process_news_dates import process_news_dates

chrome_options = Options()     
chrome_options.add_argument('--headless')     
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('start-maximized')     
chrome_options.add_argument('disable-infobars')  
# chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-extensions") 
chrome_options.add_argument('--log-level=3')

#DATE & TIME ---------------------------------------------------------------------------

def get_dates():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://tengrinews.kz")
    date_time_xpath = "//div[@class='tn-main-news-grid ']//div[contains(@class, 'tn-main-news-item')]//ul[@class='tn-data-list']/li/span//time"
    # date_times = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, date_time_xpath)))
    date_times = driver.find_elements_by_xpath(date_time_xpath)
    dates = list()
    for d in date_times:
        dates.append(d.text)

    news_dates = list()
    final_processed_news_dates = process_news_dates(dates)
    for d in final_processed_news_dates:
        news_dates.append(d)


    driver.quit()

    return news_dates

