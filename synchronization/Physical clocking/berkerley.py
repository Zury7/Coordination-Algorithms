# berkeley_algorithm.py

def berkeley_sync(clocks):
    print("Original clocks:", clocks)
    master_time = clocks[0]
    diffs = [clock - master_time for clock in clocks]
    avg_diff = sum(diffs) / len(clocks)

    synced_clocks = [clock - (diff - avg_diff) for clock, diff in zip(clocks, diffs)]
    print("Synchronized clocks:", synced_clocks)

if __name__ == "__main__":
    # Simulate 4 processes with different times (seconds)
    clocks = [100.0, 102.3, 98.5, 101.2]  # process 0 is the coordinator
    berkeley_sync(clocks)
