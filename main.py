from connectors import dummy_exchange as de
from utils.price_impact import calculate_price_impact
from utils.funding_rate_utils import calculate_apr,fetch_live_funding_rate,fetch_historical_funding_rates

def main():
    # Best Bid/Ask
    bid, ask = de.get_best_bid_ask()
    print(f"Best Bid: {bid}, Best Ask: {ask}")

    # Order Book
    bids, asks = de.get_order_book()
    print(f"Bids:\n{bids}\nAsks:\n{asks}")

    # Fetch live
    fr, interval = fetch_live_funding_rate()
    print(f"Latest funding rate: {fr} for interval {interval}h")

    # Historical + APR
    df = fetch_historical_funding_rates()
    apr = calculate_apr(df)
    print(f"Estimated APR: {apr * 100:.2f}%")

    # Price Impact
    impact = calculate_price_impact('data/dummy_order_book.csv', trade_volume=10, side='buy')
    print(f"Price Impact for $20 buy: {impact}%")

if __name__ == "__main__":
    main()
