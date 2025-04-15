class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def local_event(self):
        self.clock += 1
        print(f"Process {self.pid}: Local event → Clock = {self.clock}")

    def send_message(self, receiver):
        self.clock += 1
        print(f"Process {self.pid}: Sent message → Clock = {self.clock}")
        receiver.receive_message(self.clock, self.pid)

    def receive_message(self, timestamp, sender_pid):
        self.clock = max(self.clock, timestamp) + 1
        print(f"Process {self.pid}: Received message from Process {sender_pid} → Clock = {self.clock}")

# Example simulation
if __name__ == "__main__":
    # Create processes
    p1 = Process(1)
    p2 = Process(2)

    # Simulate events
    p1.local_event()              # e.g., compute or log
    p1.send_message(p2)           # message from p1 to p2
    p2.local_event()              # p2 does some work
    p2.send_message(p1)           # message from p2 to p1
    p1.local_event()              # p1 does more work
