import pandas as pd

def calculate_price_impact(order_book_csv, trade_volume, side):
    df = pd.read_csv(order_book_csv)
    df = df[df['side'] == ('ask' if side == 'buy' else 'bid')]
    df = df.sort_values('price', ascending=(side == 'buy'))

    total_volume = 0
    weighted_sum = 0

    for _, row in df.iterrows():
        trade_qty = min(trade_volume - total_volume, row['quantity'])
        total_volume += trade_qty
        weighted_sum += row['price'] * trade_qty
        if total_volume >= trade_volume:
            break

    avg_exec_price = weighted_sum / trade_volume
    best_bid = df[df['side'] == 'bid']['price'].max()
    best_ask = df[df['side'] == 'ask']['price'].min()
    mid_price = (best_bid + best_ask) / 2
    price_impact = ((avg_exec_price - mid_price) / mid_price) * 100

    return round(price_impact, 4)
