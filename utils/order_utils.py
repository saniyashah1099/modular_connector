import pandas as pd
import uuid
from datetime import datetime

ORDERS_FILE = 'orders/orders.csv'

def generate_order_id():
    return str(uuid.uuid4())

def place_order(exchange, pair, side, quantity, order_type, price=None):
    order_id = generate_order_id()
    timestamp = datetime.utcnow().isoformat()

    new_order = {
        'order_id': order_id,
        'exchange': exchange,
        'pair': pair,
        'side': side,
        'quantity': quantity,
        'price': price if order_type == 'LIMIT' else 'MARKET',
        'order_type': order_type,
        'status': 'OPEN',
        'timestamp': timestamp
    }

    try:
        df = pd.read_csv(ORDERS_FILE)
    except FileNotFoundError:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([new_order])], ignore_index=True)
    df.to_csv(ORDERS_FILE, index=False)
    return order_id

def cancel_order(order_id):
    df = pd.read_csv(ORDERS_FILE)
    if order_id in df['order_id'].values:
        df.loc[df['order_id'] == order_id, 'status'] = 'CANCELED'
        df.to_csv(ORDERS_FILE, index=False)
        return True
    return False

def get_order_status(order_id):
    df = pd.read_csv(ORDERS_FILE)
    if order_id in df['order_id'].values:
        return df[df['order_id'] == order_id]['status'].values[0]
    return 'NOT_FOUND'
