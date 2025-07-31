import pandas as pd
import random

PAIRS = ["BTCUSDT", "ETHUSDT"]

ORDERS_FILE = 'orders/orders.csv'

#function to generate random latest prices needed to calculate net PNL below
#This would be taken live from exchanges using APIs
def generate_random_mid_prices(PAIRS, base_price_range=(100, 30000)):
    mid_prices = {}
    for symbol in PAIRS:
        mid_price = round(random.uniform(*base_price_range), 2)
        mid_prices[symbol] = mid_price
    
    return mid_prices

def get_position_details(order_id):
    try:
        orders_df = pd.read_csv(ORDERS_FILE)
        mid_prices = generate_random_mid_prices(PAIRS)
        latest_df = pd.DataFrame(list(mid_prices.items()), columns=["pair", "latest_price"])
    except FileNotFoundError:
        raise Exception("Required data files not found.")

    if order_id not in orders_df['order_id'].values:
        raise ValueError("Order ID not found.")

    order = orders_df[orders_df['order_id'] == order_id].iloc[0]

    if order['status'] != 'FILLED':
        raise ValueError("Order is not filled. No active position.")

    pair = order['pair']
    entry_price = float(order['price']) if order['order_type'] == 'LIMIT' else 25000  # dummy market fill
    quantity = float(order['quantity'])
    side = order['side'].lower()
    timestamp = order['timestamp']
    exchange = order['exchange']

    latest_row = latest_df[latest_df['pair'] == pair]
    if latest_row.empty:
        raise ValueError(f"No market data for pair {pair}")

    latest_price = float(latest_row.iloc[0]['latest_price'])

    # NetPnL calculation
    if side == 'buy':
        pnl = (latest_price - entry_price) * quantity
        position_side = 'long'
    else:
        pnl = (entry_price - latest_price) * quantity
        position_side = 'short'

    return {
        "connector_name": exchange,
        "pair_name": pair,
        "entry_timestamp": timestamp,
        "entry_price": entry_price,
        "quantity": quantity,
        "position_side": position_side,
        "NetPnL": round(pnl, 2)
    }
