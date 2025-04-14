# ricart_agrawala.py

class Message:
    REQUEST = "REQUEST"
    REPLY = "REPLY"

    def __init__(self, msg_type, timestamp, sender_id):
        self.type = msg_type
        self.timestamp = timestamp
        self.sender_id = sender_id

    def __str__(self):
        return f"{self.type} from P{self.sender_id} at {self.timestamp}"


class Process:
    def __init__(self, pid, all_processes):
        self.pid = pid
        self.clock = 0
        self.all_processes = all_processes
        self.requesting_cs = False
        self.reply_deferred = set()
        self.replies_received = set()
        self.request_timestamp = None

    def increment_clock(self):
        self.clock += 1

    def update_clock(self, other_timestamp):
        self.clock = max(self.clock, other_timestamp) + 1

    def request_critical_section(self):
        self.increment_clock()
        self.requesting_cs = True
        self.request_timestamp = self.clock
        self.replies_received = set()

        print(f"\nP{self.pid} requesting CS at time {self.clock}")
        for p in self.all_processes:
            if p.pid != self.pid:
                p.receive_message(Message(Message.REQUEST, self.clock, self.pid))

    def receive_message(self, msg):
        self.update_clock(msg.timestamp)
        if msg.type == Message.REQUEST:
            self.handle_request(msg)
        elif msg.type == Message.REPLY:
            self.handle_reply(msg)

    def handle_request(self, msg):
        print(f"P{self.pid} received {msg}")
        send_reply = False

        if not self.requesting_cs:
            send_reply = True
        elif (msg.timestamp, msg.sender_id) < (self.request_timestamp, self.pid):
            send_reply = True
        else:
            print(f"P{self.pid} deferring reply to P{msg.sender_id}")
            self.reply_deferred.add(msg.sender_id)

        if send_reply:
            self.send_reply(msg.sender_id)

    def handle_reply(self, msg):
        print(f"P{self.pid} received {msg}")
        self.replies_received.add(msg.sender_id)
        if self.replies_received == {p.pid for p in self.all_processes if p.pid != self.pid}:
            self.enter_critical_section()

    def send_reply(self, dest_pid):
        dest = next(p for p in self.all_processes if p.pid == dest_pid)
        print(f"P{self.pid} sends REPLY to P{dest_pid}")
        dest.receive_message(Message(Message.REPLY, self.clock, self.pid))

    def enter_critical_section(self):
        print(f"\n🟢 P{self.pid} entering critical section")
        self.exit_critical_section()

    def exit_critical_section(self):
        print(f"🔴 P{self.pid} exiting critical section\n")
        self.requesting_cs = False
        for pid in self.reply_deferred:
            self.send_reply(pid)
        self.reply_deferred.clear()
        self.request_timestamp = None


# === Simulation ===
if __name__ == "__main__":
    # Create processes
    processes = [Process(pid, None) for pid in [1, 2, 3]]
    for p in processes:
        p.all_processes = processes

    # Simulate CS request from multiple processes
    processes[0].request_critical_section()  # P1
    processes[1].request_critical_section()  # P2 (simultaneous or close)
    processes[2].request_critical_section()  # P3
