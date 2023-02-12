import time
import requests
from bs4 import BeautifulSoup

class Binance_BTC_USDT:
    """ WE CHECK BTC PRICE FROM BINANCE EXCHANGE """
    
    BTC_USDT = 'https://www.binance.com/uk-UA/price/bitcoin'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    price_BTC_USDT = 0

    def __init__(self) -> None:
        self.price_BTC_USDT = float(self.get_BTC_price().replace("$", "").replace("," , ""))
        print(self.price_BTC_USDT)
        
    def get_BTC_price(self):
        full_page = requests.get(self.BTC_USDT, headers= self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "css-1267ixm", "class": "css-12ujz79"})
        return convert[0].text

class Binance_ETH_USDT:
    """ WE CHECK ETH PRICE FROM BINANCE EXCHANGE """

    ETH_USDT = 'https://www.binance.com/uk/price/ethereum'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    price_ETH_USDT = 0

    def __init__(self) -> None:
        self.price_ETH_USDT = float(self.get_ETH_price().replace("$", "").replace("," , ""))
        print(self.price_ETH_USDT )
        

    def get_ETH_price(self):
        full_page = requests.get(self.ETH_USDT, headers= self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "css-1267ixm", "class": "css-12ujz79"})
        return convert[0].text
        

class Binance_DOGE_USDT:
    """ WE CHECK DOGE PRICE FROM BINANCE EXCHANGE """

    DOGE_USDT = 'https://www.binance.com/uk/price/dogecoin'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    price_DOGE_USDT= 0 

    def __init__(self) -> None:
        self.price_DOGE_USDT = float(self.get_DOGE_price().replace("$", "").replace("," , ""))
        print(self.price_DOGE_USDT)

    def get_DOGE_price(self):
        full_page = requests.get(self.DOGE_USDT, headers= self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "css-1267ixm", "class": "css-12ujz79"})
        return convert[0].text
