from .scrape import get_thestars,get_malaysiastock,get_aljazeera,get_bloomberg,get_intraday,get_investing,get_tradingview
from .serializers import NewsSerializer, IndexPriceSerializer
from .models import News, IndexPrice
from .scrapeIndex import *

def scrape():
    news_list = []
    print('- Start scraping local news.')
    news_list.extend(get_thestars())
    news_list.extend(get_malaysiastock())
    news_list.extend(get_intraday())

    total_add = 0
    total_redundant = 0
    total_scraped = len(news_list)
    for news in news_list:
        if News.objects.filter(headline=news['headline']).exists() or News.objects.filter(url=news['url']).exists():
            total_redundant += 1
        else:
            serializer = NewsSerializer(data=news)
            if serializer.is_valid():
                serializer.save()
                total_add += 1
    print(f'- Web scraping process for local news done. {total_add} news from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')

    news_list.clear()
    print('- Start scraping international news.')
    news_list.extend(get_aljazeera())
    news_list.extend(get_investing())
    news_list.extend(get_bloomberg())

    total_add = 0
    total_redundant = 0
    total_scraped = len(news_list)
    for news in news_list:
        if News.objects.filter(headline=news['headline']).exists() or News.objects.filter(url=news['url']).exists():
            total_redundant += 1
        else:
            serializer = NewsSerializer(data=news)
            if serializer.is_valid():
                serializer.save()
                total_add += 1
    
    print(f'- Web scraping process for international news done. {total_add} news from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')

    news_list.clear()
    print('- Start scraping market ideas.')
    news_list.extend(get_tradingview())

    total_add = 0
    total_redundant = 0
    total_scraped = len(news_list)
    for news in news_list:
        if News.objects.filter(headline=news['headline']).exists() or News.objects.filter(url=news['url']).exists():
            total_redundant += 1
        else:
            serializer = NewsSerializer(data=news)
            if serializer.is_valid():
                serializer.save()
                total_add += 1
    print(f'- Web scraping process for market ideas done. {total_add} news from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')

def scrape_stock_price():
    price_list = []
    print('Scraping Index Prices from yAhoo fInAnce')
    price_list.extend(get_snp500Futures())
    price_list.extend(get_snp500Standard())
    price_list.extend(get_gold())

    total_add = 0
    total_redundant = 0
    total_scraped = len(price_list)

    for price in price_list:
        if IndexPrice.objects.filter(productName=price['productName']).exists():
            total_redundant += 1
        else: 
            serializer = IndexPriceSerializer(data=price)
            if serializer.is_valid():
                serializer.save()
                total_add += 1   
    print(f'- Web scraping process for Index Price done. {total_add} price from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')
    price_list.clear()


    price_list.extend(get_nikkei225())
    price_list.extend(get_KLCI())
    price_list.extend(get_bitcoin_cash())
    price_list.extend(get_lite_coin())

    total_add = 0
    total_redundant = 0
    total_scraped = len(price_list)

    for price in price_list:
        if IndexPrice.objects.filter(productName=price['productName']).exists():
            total_redundant += 1
        else: 
            serializer = IndexPriceSerializer(data=price)
            if serializer.is_valid():
                serializer.save()
                total_add += 1   
    print(f'- Web scraping process for Index Price done. {total_add} price from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')
    price_list.clear()


    price_list.extend(get_dowFutures())
    price_list.extend(get_dowJones())
    price_list.extend(get_russellFutures())
    price_list.extend(get_russsell2000())

    total_add = 0
    total_redundant = 0
    total_scraped = len(price_list)

    for price in price_list:
        if IndexPrice.objects.filter(productName=price['productName']).exists():
            total_redundant += 1
        else: 
            serializer = IndexPriceSerializer(data=price)
            if serializer.is_valid():
                serializer.save()
                total_add += 1   
    print(f'- Web scraping process for Index Price done. {total_add} price from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')
    price_list.clear()


    price_list.extend(get_ethereum())
    price_list.extend(get_ripple())
    price_list.extend(get_crudeOil())
    price_list.extend(get_bitcoin())


    total_add = 0
    total_redundant = 0
    total_scraped = len(price_list)

    for price in price_list:
        if IndexPrice.objects.filter(productName=price['productName']).exists():
            total_redundant += 1
        else: 
            serializer = IndexPriceSerializer(data=price)
            if serializer.is_valid():
                serializer.save()
                total_add += 1   
    print(f'- Web scraping process for Index Price done. {total_add} news from {total_scraped} scraped are added to database. Total redundant news is {total_redundant}')
        