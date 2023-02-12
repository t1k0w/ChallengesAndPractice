import requests
from bs4 import BeautifulSoup
import time
from Binance_Values import *


btc_price = 0
eth_price = 0 
doge_price = 0 

def checker(a = 0 , b = 0, c = 0):
   a = Binance_BTC_USDT()
   b = Binance_ETH_USDT()
   c = Binance_DOGE_USDT()

   btc_price = a
   eth_price = b
   doge_price = c 

def compare(): 
    #checker()
    DOGE_price = Binance_DOGE_USDT()
    #BTC_price = Binance_ETH_USDT()
    #ETH_price = Binance_DOGE_USDT()

    last_doge_price = float(Binance_DOGE_USDT.get_DOGE_price(DOGE_price).replace("$", "").replace("," , ""))
    #last_btc_price = BTC_price
    #last_eth_price = ETH_price
    print(last_doge_price)


def main():
    compare()

if __name__ == "__main__":
    main()
