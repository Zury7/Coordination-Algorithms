# christians_algorithm.py

import time
import random

def simulate_network_delay():
    return random.uniform(0.05, 0.1)  # 50-100ms

def server_time():
    return time.time()

def client_sync():
    t0 = time.time()
    delay1 = simulate_network_delay()
    time.sleep(delay1)

    ts = server_time()

    delay2 = simulate_network_delay()
    time.sleep(delay2)
    t1 = time.time()

    RTT = t1 - t0
    estimated_server_time = ts + RTT / 2

    print(f"Client original time: {t0}")
    print(f"Server time at send: {ts}")
    print(f"RTT: {RTT:.4f} sec")
    print(f"Estimated server time: {estimated_server_time}")
    print(f"Client adjusted time: {estimated_server_time}")

if __name__ == "__main__":
    client_sync()
