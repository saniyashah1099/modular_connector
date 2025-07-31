import asyncio
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from sqlalchemy import create_engine
from combined_order_book import combined_order_book

async def collect_and_store(engine, interval=1):
    while True:
        snapshot = combined_order_book()
        snapshot.to_sql("order_book_snapshots", engine, if_exists="append", index=False)
        print(snapshot.iloc[0].timestamp)
        await asyncio.sleep(interval)


if __name__ == "__main__":
    # Create DB engine
    engine = create_engine('postgresql://saniyashah:your_secure_password@localhost:5432/dummy')

    # Run the async collector
    asyncio.run(collect_and_store(engine))