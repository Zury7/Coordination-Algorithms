# token_ring.py

import time

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.has_token = False
        self.next_process = None

    def set_next(self, next_proc):
        self.next_process = next_proc

    def receive_token(self):
        self.has_token = True
        print(f"🔵 P{self.pid} received the token.")
        self.enter_critical_section()

    def enter_critical_section(self):
        if self.has_token:
            print(f"🟢 P{self.pid} entering critical section.")
            time.sleep(1)  # Simulate doing work in CS
            print(f"🔴 P{self.pid} exiting critical section.")
            self.pass_token()

    def pass_token(self):
        self.has_token = False
        print(f"➡️  P{self.pid} passing token to P{self.next_process.pid}\n")
        self.next_process.receive_token()


# === Simulation ===
if __name__ == "__main__":
    # Create processes in a ring
    processes = [Process(pid) for pid in [1, 2, 3, 4]]
    n = len(processes)

    for i in range(n):
        processes[i].set_next(processes[(i + 1) % n])  # Circular ring

    # Start token at P1
    processes[0].has_token = True
    processes[0].enter_critical_section()
