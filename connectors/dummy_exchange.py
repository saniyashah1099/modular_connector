import pandas as pd

def get_best_bid_ask(order_book_df):
    best_bid = order_book_df[order_book_df["side"] == "bid"].sort_values(by="price", ascending=False).iloc[0]
    best_ask = order_book_df[order_book_df["side"] == "ask"].sort_values(by="price", ascending=True).iloc[0]
    return best_bid["price"], best_ask["price"]

def get_funding_rates():
    df = pd.read_csv('data/dummy_funding.csv')
    return df

def get_latest_funding_rate():
    df = pd.read_csv('data/dummy_funding.csv')
    return df.iloc[-1]['funding_rate']
