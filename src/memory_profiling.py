
import gc
import tracemalloc
import matplotlib.pyplot as plt

# ==========================================
# NODE
# ==========================================

class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.next = None


# ==========================================
# SINGLY LINKED LIST
# ==========================================

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_tail(self, pid, burst_time):
        new_node = Node(pid, burst_time)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


# ==========================================
# MEMORY PROFILING
# ==========================================

DATA_SIZES = [100, 1000, 10000, 100000]
memory_results = []

print("=" * 60)
print("MEMORY PROFILING - SINGLY LINKED LIST")
print("=" * 60)

for size in DATA_SIZES:
    gc.collect()
    tracemalloc.start()

    linked_list = SinglyLinkedList()

    # Memori sebelum node dibuat
    before, _ = tracemalloc.get_traced_memory()

    # Membuat node sesuai ukuran data
    for i in range(size):
        linked_list.insert_at_tail(f"P{i+1}", 5)

    # Memori setelah seluruh node dibuat
    current, peak = tracemalloc.get_traced_memory()

    # Menggunakan current memory agar objek masih tersimpan
    memory_kb = (current - before) / 1024
    memory_results.append(memory_kb)

    print(f"{size:>7} node | {memory_kb:>10.2f} KB")

    tracemalloc.stop()
    del linked_list
    gc.collect()

print("=" * 60)

# ==========================================
# GRAPH MEMORY
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    DATA_SIZES,
    memory_results,
    marker="o",
    linewidth=2
)

plt.xscale("log")
plt.xticks(DATA_SIZES, ["100", "1.000", "10.000", "100.000"])

plt.xlabel("Jumlah Node")
plt.ylabel("Konsumsi Memori (KB)")
plt.title("Memory Profiling - Singly Linked List")
plt.grid(True)
plt.tight_layout()

# Simpan grafik di folder src
plt.savefig("grafik_memory_singly_linked_list.png", dpi=300)

plt.show()

print("Grafik berhasil disimpan:")
print("grafik_memory_singly_linked_list.png")
