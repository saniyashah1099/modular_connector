import pandas as pd
from datetime import datetime

def fetch_live_funding_rate(filepath='data/dummy_funding.csv', exchange='binance', pair='BTCUSDT'):
    """
    Fetch the most recent funding rate from a dummy CSV file.
    """
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    df = df[(df['exchange'] == exchange) & (df['pair'] == pair)]
    latest_row = df.sort_values('timestamp', ascending=False).iloc[0]
    return latest_row['funding_rate'], latest_row['interval_hours']


def fetch_historical_funding_rates(filepath='data/dummy_funding.csv', exchange='binance', pair='BTCUSDT'):
    """
    Fetch historical funding rate data as a DataFrame.
    """
    df = pd.read_csv(filepath, parse_dates=['timestamp'])
    return df[(df['exchange'] == exchange) & (df['pair'] == pair)].sort_values('timestamp')


def calculate_apr(funding_rates_df):
    """
    Estimate aggregated APR from historical funding rates.
    
    Parameters:
        funding_rates_df (DataFrame): Should contain 'funding_rate' and 'interval_hours' columns.

    Returns:
        APR as a percentage (annualized return)
    """
    total_apr = 0.0

    for _, row in funding_rates_df.iterrows():
        rate = row['funding_rate']
        interval_hours = row['interval_hours']
        annualised_factor = 365
        periods_per_year = annualised_factor * 24 / interval_hours
        total_apr += rate * periods_per_year

    return round(total_apr, 4)
