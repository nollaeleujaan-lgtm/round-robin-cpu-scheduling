
# ==========================================
# PROYEK ROUND ROBIN CPU SCHEDULING
# File: node.py
# ==========================================

class Node:
    """
    Class Node digunakan untuk menyimpan
    informasi setiap proses CPU.
    """

    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time

        # Pointer menuju node berikutnya
        self.next = None

# ==========================================
# PENGUJIAN CLASS NODE
# ==========================================

if __name__ == "__main__":
    proses = Node("P1", 5)

    print("ID Proses:", proses.pid)
    print("Burst Time:", proses.burst_time)
    print("Remaining Time:", proses.remaining_time)
    print("Next:", proses.next)