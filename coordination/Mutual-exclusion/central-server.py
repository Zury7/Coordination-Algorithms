# centralized_mutex.py

import time
import random


class Coordinator:
    def __init__(self):
        self.locked_by = None
        self.queue = []

    def request_cs(self, pid):
        if self.locked_by is None:
            print(f"✅ Coordinator grants access to P{pid}")
            self.locked_by = pid
            return True
        else:
            print(f"⏳ Coordinator queues P{pid}")
            self.queue.append(pid)
            return False

    def release_cs(self, pid):
        if self.locked_by == pid:
            print(f"🔓 P{pid} releases CS")
            self.locked_by = None
            if self.queue:
                next_pid = self.queue.pop(0)
                print(f"➡️ Coordinator now grants access to P{next_pid}")
                self.locked_by = next_pid
                return next_pid
        return None


class Process:
    def __init__(self, pid, coordinator):
        self.pid = pid
        self.coordinator = coordinator

    def request_critical_section(self):
        print(f"\n🔄 P{self.pid} requesting critical section")
        granted = self.coordinator.request_cs(self.pid)
        while not granted:
            time.sleep(random.uniform(0.5, 1.0))  # Wait before retrying
            granted = (self.coordinator.locked_by == self.pid)
        self.enter_critical_section()

    def enter_critical_section(self):
        print(f"🟢 P{self.pid} ENTERING critical section")
        time.sleep(1)  # Simulate work
        print(f"🔴 P{self.pid} EXITING critical section")
        next_pid = self.coordinator.release_cs(self.pid)
        if next_pid:
            # Notify next process immediately (simulate instant notification)
            next_process = process_map[next_pid]
            next_process.enter_critical_section()


# === Simulation ===
if __name__ == "__main__":
    coordinator = Coordinator()
    process_list = [Process(pid, coordinator) for pid in [1, 2, 3]]
    process_map = {p.pid: p for p in process_list}

    for process in process_list:
        process.request_critical_section()
