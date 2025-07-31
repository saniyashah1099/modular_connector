import time
import random
from utils.order_utils import place_order, cancel_order, get_order_status

def performance_test(n_orders=200):
    start_time = time.time()
    success = 0
    failure = 0
    latencies = []

    for i in range(n_orders):
        order_type = random.choice(["LIMIT", "MARKET"])
        side = random.choice(["buy", "sell"])
        quantity = random.randint(1, 10)
        price = round(random.uniform(1000, 2000), 2) if order_type == "LIMIT" else None

        t0 = time.time()
        try:
            order_id = place_order("dummyex", "BTCUSDT", side, quantity, order_type, price)
            cancel_order(order_id)
            latency = time.time() - t0
            latencies.append(latency)
            success += 1
        except Exception as e:
            failure += 1

    total_time = time.time() - start_time
    avg_latency = sum(latencies) / len(latencies) if latencies else 0

    print("\n")
    print(f"*************************************************")
    print(f"Performance Test Results:")
    print(f"- Total orders attempted: {n_orders}")
    print(f"- Success: {success}, Failure: {failure}")
    print(f"- Average latency: {avg_latency:.4f} sec")
    print(f"- Total execution time: {total_time:.2f} sec")
    print(f"*************************************************")
    print("\n")
