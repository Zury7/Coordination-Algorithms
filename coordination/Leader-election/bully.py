# bully_election.py

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.alive = True

    def __str__(self):
        return f"P{self.pid}"


class BullyElection:
    def __init__(self, processes):
        self.processes = sorted(processes, key=lambda p: p.pid)
        self.leader = None

    def start_election(self, initiator_pid):
        initiator = self.get_process_by_pid(initiator_pid)
        print(f"\n{initiator} starts an election")

        higher_processes = [p for p in self.processes if p.pid > initiator.pid and p.alive]

        if not higher_processes:
            self.declare_leader(initiator)
            return

        for p in higher_processes:
            print(f"{initiator} sends ELECTION to {p}")
            print(f"{p} replies OK")

        # Now higher processes take over the election
        for p in reversed(higher_processes):
            self.start_election(p.pid)
            return  # Let the highest one win

    def declare_leader(self, process):
        self.leader = process
        print(f"{process} becomes the new LEADER")
        self.broadcast_leader(process)

    def broadcast_leader(self, leader):
        print(f"\nBroadcasting COORDINATOR: {leader}")
        for p in self.processes:
            if p.alive and p.pid != leader.pid:
                print(f"{p} acknowledges {leader} as leader")

    def get_process_by_pid(self, pid):
        return next(p for p in self.processes if p.pid == pid)


# === Simulation ===
if __name__ == "__main__":
    process_list = [Process(1), Process(2), Process(3), Process(4), Process(5)]
    bully = BullyElection(process_list)

    # Simulate process 5 (leader) is down
    process_list[-1].alive = False

    bully.start_election(2)
