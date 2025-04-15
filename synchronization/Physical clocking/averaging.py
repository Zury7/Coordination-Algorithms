# averaging_algorithm.py

def averaging_sync(clocks):
    print("Original clocks:", clocks)
    average = sum(clocks) / len(clocks)
    synced_clocks = [average] * len(clocks)
    print("All clocks set to average:", synced_clocks)

if __name__ == "__main__":
    clocks = [200.5, 198.3, 201.7, 199.9]
    averaging_sync(clocks)
