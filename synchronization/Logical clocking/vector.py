class Process:
    def __init__(self, pid, num_processes):
        self.pid = pid
        self.num_processes = num_processes
        self.clock = [0] * num_processes

    def local_event(self):
        self.clock[self.pid] += 1
        print(f"Process {self.pid}: Local event → Clock = {self.clock}")

    def send_message(self, receiver):
        self.clock[self.pid] += 1
        print(f"Process {self.pid}: Sent message → Clock = {self.clock}")
        receiver.receive_message(self.clock, self.pid)

    def receive_message(self, received_clock, sender_pid):
        for i in range(self.num_processes):
            self.clock[i] = max(self.clock[i], received_clock[i])
        self.clock[self.pid] += 1
        print(f"Process {self.pid}: Received message from Process {sender_pid} → Clock = {self.clock}")

# Example simulation
if __name__ == "__main__":
    num_processes = 3
    p0 = Process(0, num_processes)
    p1 = Process(1, num_processes)
    p2 = Process(2, num_processes)

    # Simulate some events
    p0.local_event()
    p0.send_message(p1)
    p1.local_event()
    p1.send_message(p2)
    p2.local_event()
    p2.send_message(p0)
