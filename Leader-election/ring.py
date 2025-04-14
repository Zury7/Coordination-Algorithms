# ring_election.py

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.participant = False
        self.alive = True

    def __str__(self):
        return f"P{self.pid}"


class RingElection:
    def __init__(self, processes):
        self.processes = sorted(processes, key=lambda p: p.pid)
        self.n = len(self.processes)

    def get_successor(self, index):
        return (index + 1) % self.n

    def start_election(self, initiator_index):
        print(f"\nElection initiated by {self.processes[initiator_index]}")
        msg_id = self.processes[initiator_index].pid
        self.processes[initiator_index].participant = True

        index = self.get_successor(initiator_index)
        while True:
            current = self.processes[index]
            if not current.alive:
                index = self.get_successor(index)
                continue

            print(f"Process {current} received ELECTION({msg_id})")

            if current.pid > msg_id:
                msg_id = current.pid
                current.participant = True
            elif current.pid < msg_id and not current.participant:
                msg_id = current.pid
                current.participant = True
            elif current.pid == msg_id:
                print(f"Process {current} becomes the LEADER")
                self.announce_leader(current.pid)
                break

            index = self.get_successor(index)

    def announce_leader(self, leader_id):
        print(f"\nAnnouncing leader: P{leader_id}")
        for p in self.processes:
            if p.alive:
                p.participant = False
                print(f"{p} acknowledges P{leader_id} as leader")


# === Simulation ===
if __name__ == "__main__":
    process_list = [Process(1), Process(3), Process(5), Process(7), Process(9)]
    ring = RingElection(process_list)

    # Simulate failure of highest process
    process_list[-1].alive = False

    ring.start_election(1)
