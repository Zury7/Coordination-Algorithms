# quorum_mutex.py

import random
import time

class Coordinator:
    def __init__(self, cid):
        self.cid = cid
        self.locked_by = None

    def handle_request(self, pid):
        if self.locked_by is None:
            self.locked_by = pid
            print(f"✅ Coordinator {self.cid} grants permission to P{pid}")
            return True
        else:
            print(f"⛔ Coordinator {self.cid} denies permission to P{pid} (held by P{self.locked_by})")
            return False

    def release(self, pid):
        if self.locked_by == pid:
            print(f"🔓 Coordinator {self.cid} releases lock from P{pid}")
            self.locked_by = None


class Process:
    def __init__(self, pid, coordinators, quorum_size):
        self.pid = pid
        self.coordinators = coordinators
        self.quorum_size = quorum_size

    def request_critical_section(self):
        print(f"\n🔄 P{self.pid} requesting critical section...")
        approvals = []
        for coord in self.coordinators:
            if coord.handle_request(self.pid):
                approvals.append(coord)
            if len(approvals) >= self.quorum_size:
                break

        if len(approvals) >= self.quorum_size:
            self.enter_critical_section()
            for coord in approvals:
                coord.release(self.pid)
        else:
            print(f"⚠️ P{self.pid} failed to get quorum. Backing off...\n")
            for coord in approvals:
                coord.release(self.pid)
            time.sleep(random.uniform(1, 2))  # Back-off
            self.request_critical_section()

    def enter_critical_section(self):
        print(f"🟢 P{self.pid} ENTERING critical section")
        time.sleep(1)  # Simulate work
        print(f"🔴 P{self.pid} EXITING critical section")


# === Simulation ===
if __name__ == "__main__":
    coordinators = [Coordinator(cid) for cid in [1, 2, 3]]
    quorum_size = 2  # Majority

    processes = [Process(pid, coordinators, quorum_size) for pid in [1, 2, 3]]

    # Simulate concurrent requests (sequentially in this simulation)
    for p in processes:
        p.request_critical_section()
