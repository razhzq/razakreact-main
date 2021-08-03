import time
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime as dt
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_snp500Futures():
  print('scraping S&P 500 Futures data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/ES%3DF?p=ES%3DF')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
        print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'S&P Futures',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping S&P Futures failed')
  finally:
    return market_price_list

def get_snp500Standard():
  print('scraping S&P 500 Standard data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC&.tsrc=fin-srch')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'S&P 500',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping S&P 500 Standard failed')
  finally:
    return market_price_list

def get_gold():
  print('scraping Gold data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'Gold',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping Gold failed')
  finally:
    return market_price_list

def get_nikkei225():
  print('scraping Nikkei 225 data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/%5EN225?p=^N225&.tsrc=fin-srch')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'Nikkei 225',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping Nikkei 225 failed')
  finally:
    return market_price_list

def get_KLCI():
  print('scraping KLCI data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/%5EKLSE?p=^KLSE&.tsrc=fin-srch')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'KLCI',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping KLCI failed')
  finally:
    return market_price_list

def get_nasdaq_composite():
  print('scraping Nasdaq Composite data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'NASDAQ',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping Nasdaq Composite failed')
  finally:
    return market_price_list

def get_nasdaq_future():
  print('scraping Nasdaq Future data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/NQ%3DF?p=NQ%3DF')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'NASDAQ Futures',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping Nasdaq Futures failed')
  finally:
    return market_price_list

def get_bitcoin_cash():
  print('scraping Bitcoin Cash data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/BCH-USD?p=BCH-USD&.tsrc=fin-srch')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'Bitcoin Cash',
      'currentMarketPrice': current_price,
      # 'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping Bitcoin Cash failed')
  finally:
    return market_price_list

def get_lite_coin():
  print('scraping Lite Coin data')
  market_price_list = []
  try:
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'scrape/chromedriver.exe',options=options)
    driver.get('https://finance.yahoo.com/quote/LTC-USD?p=LTC-USD&.tsrc=fin-srch')
    page = driver.page_source
    page_soup = BeautifulSoup(page, "html.parser")
    current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
    '''
    current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}),'text',None)
    if current_price_point_change:
      print('percentage succeed')
    else:
      current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}),'text',None)
    '''
    new_price = {
      'productName' : 'Lite Coin',
      'currentMarketPrice': current_price,
      #'priceChangePercentage': current_price_point_change,
    }

    market_price_list.append(new_price)
    driver.quit()

  except:
    print('Scraping Lite Coin failed')
  finally:
    return market_price_list

def get_dowFutures():
    print('Scraping Dow Futures Data')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/YM%3DF?p=YM%3DF')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'Dow Futures',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Dow Futures Failed')
    finally:
        return market_price_list 

def get_dowJones():
    print('Scraping Dow Jones')
    market_price_list= []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/%5EDJI?p=^DJI&.tsrc=fin-srch')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'Dow Jones',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Dow Jones Failed')
    finally:
        return market_price_list 

def get_russsell2000():
    print('Scrapping Russell2000')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/%5ERUT?p=^RUT&.tsrc=fin-srch')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'Russell2000',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Rusell2000 Failed')
    finally:
        return market_price_list 

def get_russellFutures():
    print('Scrapping Russell Futures')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/RTY%3DF?p=RTY%3DF')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'Russell2000 Futures',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Russell2000 Futures Failed')
    finally:
        return market_price_list 

def get_crudeOil():
    print('Scraping Crude Oil')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/CL%3DF?p=CL%3DF')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'Crude Oil',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Crude Oil Failed')
    finally:
        return market_price_list 

def get_bitcoin():
    print('Scraping Bitcoin')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'BTC USD',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Bitcoin Failed')
    finally:
        return market_price_list 

def get_ethereum():
    print('Scraping Ethereum')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'ETH USD',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Ethereum Failed')
    finally:
        return market_price_list 

def get_ripple():
    print('Scrapping Ripple')
    market_price_list = []
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_experimental_option ('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='scrape/chromedriver.exe', options=options)
        driver.get('https://finance.yahoo.com/quote/XRP-USD?p=XRP-USD')
        page = driver.page_source
        page_soup = BeautifulSoup(page,"html.parser")
        current_price = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span',attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}),'text',None)
        '''
        current_price_point_change = getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor'}),'text',None)
        if current_price_point_change:
            print("Percentage Succeed")
        else:
            current_price_point_change =  getattr(page_soup.find('div', attrs={'class': 'D(ib) Mend(20px)'}).find('span', attrs={'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor'}),'text',None)
        '''
        new_price = {
            'productName' : 'XRP USD',
            'currentMarketPrice' : current_price,
            #'currentMarketPriceChange' : current_price_point_change,
        }

        market_price_list.append(new_price)
        driver.quit()

    except:
        print('Scraping Ripple Failed')
    finally:
        return market_price_list 