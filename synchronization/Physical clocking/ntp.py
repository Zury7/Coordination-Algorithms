# ntp_algorithm.py

import time
import random

def simulate_network_delay():
    return random.uniform(0.02, 0.05)

def server_time():
    return time.time()

def ntp_sync():
    t1 = time.time()  # client's send time
    delay1 = simulate_network_delay()
    time.sleep(delay1)

    t2 = server_time()  # server's receive time
    t3 = server_time()  # server's reply time

    delay2 = simulate_network_delay()
    time.sleep(delay2)
    t4 = time.time()  # client's receive time

    offset = ((t2 - t1) + (t3 - t4)) / 2
    delay = (t4 - t1) - (t3 - t2)

    print(f"Client send time (t1): {t1}")
    print(f"Server receive time (t2): {t2}")
    print(f"Server reply time (t3): {t3}")
    print(f"Client receive time (t4): {t4}")
    print(f"Estimated offset: {offset:.6f} sec")
    print(f"Estimated network delay: {delay:.6f} sec")
    print(f"Adjusted client time: {t4 + offset}")

if __name__ == "__main__":
    ntp_sync()
