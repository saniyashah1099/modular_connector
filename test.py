import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://saniyashah:your_secure_password@localhost:5432/dummy')

# Sample DataFrame (should include timestamp)
df = pd.DataFrame({
    'timestamp': pd.date_range(start='2023-01-01', periods=5, freq='T'),
    'exchange': ['binance']*5,
    'pair': ['BTC/USDT']*5,
    'bids': [[(10000, 1)], [(10001, 1.1)], [(9999, 1.2)], [(10002, 1.3)], [(9998, 1.5)]],
    'asks': [[(10010, 1)], [(10011, 1.1)], [(10009, 1.2)], [(10012, 1.3)], [(10008, 1.5)]],
})

# Send to TimescaleDB (replace "order_book_snapshots" with your table name)
df.to_sql("order_book_snapshots", engine, if_exists='append', index=False)





