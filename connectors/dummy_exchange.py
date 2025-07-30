import pandas as pd

def get_best_bid_ask():
    df = pd.read_csv('data/dummy_order_book.csv')
    best_bid = df[df['side'] == 'bid']['price'].max()
    best_ask = df[df['side'] == 'ask']['price'].min()
    return best_bid, best_ask

def get_order_book():
    df = pd.read_csv('data/dummy_order_book.csv')
    return df[df['side'] == 'bid'], df[df['side'] == 'ask']

def get_funding_rates():
    df = pd.read_csv('data/dummy_funding.csv')
    return df

def get_latest_funding_rate():
    df = pd.read_csv('data/dummy_funding.csv')
    return df.iloc[-1]['funding_rate']
