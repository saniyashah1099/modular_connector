# def generate_dummy_order_book(n_levels=10, mid_price=30000, spread=10, depth_variation=5):
#     # Generate ascending ask prices
#     ask_prices = np.round(mid_price + np.linspace(spread / 2, spread / 2 + n_levels, n_levels), 2)
#     ask_qtys = np.round(np.random.uniform(0.1, depth_variation, n_levels), 4)

#     # Generate descending bid prices
#     bid_prices = np.round(mid_price - np.linspace(spread / 2, spread / 2 + n_levels, n_levels), 2)
#     bid_qtys = np.round(np.random.uniform(0.1, depth_variation, n_levels), 4)

#     # Create DataFrame
#     asks = pd.DataFrame({"price": ask_prices, "quantity": ask_qtys, "side": "ask"})
#     bids = pd.DataFrame({"price": bid_prices, "quantity": bid_qtys, "side": "bid"})

#     # Combine and return
#     order_book = pd.concat([asks, bids], ignore_index=True)
#     return order_book
import pandas as pd
import numpy as np
from datetime import datetime

COMMON_PAIRS = [
    "BTC/USDT", "ETH/USDT", "BTC/ETH",
    "LTC/BTC", "DOGE/USDT"
]

def generate_dummy_order_book(exchange, pair, n_levels=10, mid_price=1, spread=0.001, depth_variation=5):
    # Set realistic mid_price per pair
    if pair == "BTC/USDT":
        mid = 30000
    elif pair == "ETH/USDT":
        mid = 2000
    elif pair == "BTC/ETH":
        mid = 15  # 1 BTC ≈ 15 ETH
    elif pair == "LTC/BTC":
        mid = 0.004
    elif pair == "DOGE/USDT":
        mid = 0.22
    else:
        mid = mid_price

    ask_prices = np.round(mid + np.linspace(spread / 2, spread / 2 + n_levels*spread, n_levels), 6)
    ask_qtys = np.round(np.random.uniform(0.1, depth_variation, n_levels), 4)
    bid_prices = np.round(mid - np.linspace(spread / 2, spread / 2 + n_levels*spread, n_levels), 6)
    bid_qtys = np.round(np.random.uniform(0.1, depth_variation, n_levels), 4)
    ts = datetime.utcnow().isoformat()

    asks = pd.DataFrame({
        "timestamp": ts, "exchange": exchange, "pair_name": pair,
        "side": "ask", "price": ask_prices, "quantity": ask_qtys
    })
    bids = pd.DataFrame({
        "timestamp": ts, "exchange": exchange, "pair_name": pair,
        "side": "bid", "price": bid_prices, "quantity": bid_qtys
    })
    return pd.concat([asks, bids], ignore_index=True)

def get_best_bid_ask(df):
    best_bid = df[df["side"] == "bid"].nlargest(1, "price").iloc[0]["price"]
    best_ask = df[df["side"] == "ask"].nsmallest(1, "price").iloc[0]["price"]
    return best_bid, best_ask

if __name__ == "__main__":
    exchange = "dummy_exchange"
    summary = []

    for pair in COMMON_PAIRS:
        ob = generate_dummy_order_book(exchange, pair)
        bid, ask = get_best_bid_ask(ob)
        summary.append({"exchange": exchange, "pair": pair, "best_bid": bid, "best_ask": ask})
        print(f"\nOrder Book for {pair}:\n", ob.head())
    
    print("\n=== Best Bid/Ask Summary ===")
    print(pd.DataFrame(summary))
