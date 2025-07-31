from connectors import dummy_exchange as de
import pandas as pd
from connectors.dummy_order_book import generate_dummy_order_book

EXCHANGES = 'binance','bitmart','derive'
PAIRS = "BTC/USDT", "ETH/USDT", "BTC/ETH","LTC/BTC", "DOGE/USDT"

def combined_order_book():
    exchange_pair_list = [(ex, pair) for ex in EXCHANGES for pair in PAIRS]
    order_book = pd.DataFrame()
    for exchange_pair in exchange_pair_list:
        order_book = pd.concat([order_book,generate_dummy_order_book(exchange_pair[0],exchange_pair[1])])
    

    return order_book
