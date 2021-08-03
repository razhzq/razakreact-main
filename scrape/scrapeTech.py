import time
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime as dt
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytz import timezone

def get_cnet():
    print('scraping CNET TECH')
    news_list = []
    try:
        options = Options()
        options.headless = True
        options.add_argument("--log-level=OFF")
        driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
        driver.get('https://www.cnet.com/tech/services-and-software/2/')
        element = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.ID,'load-more ' ))
            )
        element.click()
        time.sleep(2)
        page = driver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')