from connectors import dummy_exchange as de
import logging
import pandas as pd
from utils.price_impact import calculate_price_impact
from utils.funding_rate_utils import calculate_apr,fetch_live_funding_rate,fetch_historical_funding_rates
from utils.performance_test import performance_test
from utils.position_tracker import get_position_details
from connectors.dummy_order_book import generate_dummy_order_book

EXCHANGES = 'binance','bitmart','derive'
PAIRS = "BTC/USDT", "ETH/USDT", "BTC/ETH","LTC/BTC", "DOGE/USDT"

def main():
    exchange_pair_list = [(ex, pair) for ex in EXCHANGES for pair in PAIRS]
    order_book = pd.DataFrame()
    for exchange_pair in exchange_pair_list:
        order_book = pd.concat([order_book,generate_dummy_order_book(exchange_pair[0],exchange_pair[1])])
    # Print the full book
    print("Full Order Book:\n", order_book)
    
    # Get best bid/ask
    best_bid, best_ask = de.get_best_bid_ask(order_book)
    print(f"\nBest Bid: {best_bid}")
    print(f"Best Ask: {best_ask}") 

    # Fetch live
    fr, interval = fetch_live_funding_rate()
    print(f"Latest funding rate: {fr} for interval {interval}h")

    # Historical + APR
    df = fetch_historical_funding_rates()
    apr = calculate_apr(df)
    print(f"Estimated APR: {apr * 100:.2f}%")
    print("\n")

    # Price Impact
    impact = calculate_price_impact(order_book, trade_volume=10, side='buy')
    print(f"Price Impact for $20 buy: {impact}%")

if __name__ == "__main__":
    main()
    
    performance_test(n_orders=200)

    #passing a dummy id to get its data
    filled_order_id = "1ca4ef89-eed9-4e89-8f82-e304f9076d57"
    position = get_position_details(filled_order_id)
    
    logging.info("🔎 Position Monitoring:")
    for key, value in position.items():
        print(f"{key}: {value}")