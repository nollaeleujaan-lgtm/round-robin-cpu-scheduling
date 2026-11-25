
import gc
import tracemalloc
import matplotlib.pyplot as plt

# ==================================================
# SINGLY LINKED LIST
# ==================================================

class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.next = None


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


# ==================================================
# MEMORY PROFILING
# ==================================================

DATA_SIZES = [100, 1000, 10000, 100000]
memory_results = []

print("=" * 60)
print(" MEMORY PROFILING - SINGLY LINKED LIST")
print("=" * 60)

for size in DATA_SIZES:
    gc.collect()
    tracemalloc.start()

    linked_list = SinglyLinkedList()

    # Mengukur memori sebelum pembuatan node
    before_current, _ = tracemalloc.get_traced_memory()

    # Membuat node sesuai ukuran data
    for i in range(size):
        linked_list.insert_at_tail(f"P{i+1}", 5)

    # Mengukur memori setelah node dibuat
    after_current, peak = tracemalloc.get_traced_memory()

    memory_kb = (after_current - before_current) / 1024
    memory_results.append(memory_kb)

    print(f"Jumlah Node: {size:>6} | Memori: {memory_kb:>10.2f} KB")

    tracemalloc.stop()

    # Membersihkan data sebelum pengujian berikutnya
    del linked_list
    gc.collect()

print("=" * 60)

# ==================================================
# GRAPH
# ==================================================

plt.figure(figsize=(9, 5))

plt.plot(
    DATA_SIZES,
    memory_results,
    marker="o",
    linewidth=2
)

plt.xscale("log")
plt.xlabel("Jumlah Node")
plt.ylabel("Konsumsi Memori (KB)")
plt.title("Memory Profiling - Singly Linked List")

plt.xticks(DATA_SIZES, ["100", "1.000", "10.000", "100.000"])
plt.grid(True)
plt.tight_layout()

# Simpan grafik
plt.savefig("grafik_memory_singly_linked_list.png", dpi=300)

# Tampilkan grafik
plt.show()

print("Grafik berhasil disimpan:")
print("grafik_memory_singly_linked_list.png")
