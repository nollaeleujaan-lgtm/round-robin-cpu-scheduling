
from node import Node


class SinglyLinkedList:
    """
    Singly Linked List untuk mengelola antrean proses CPU.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    # ==========================================
    # INSERT OPERATIONS
    # ==========================================

    def insert_at_head(self, pid, burst_time):
        """Menambahkan proses pada bagian depan Linked List."""
        new_node = Node(pid, burst_time)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return new_node

    def insert_at_index(self, pid, burst_time, index):
        """Menambahkan proses pada indeks tertentu (0-based)."""

        if index < 0:
            raise IndexError("Index tidak boleh negatif.")

        if index == 0:
            return self.insert_at_head(pid, burst_time)

        new_node = Node(pid, burst_time)
        current = self.head
        position = 0

        # Mencari node sebelum posisi penyisipan
        while current is not None and position < index - 1:
            current = current.next
            position += 1

        if current is None:
            raise IndexError("Index melebihi panjang Linked List.")

        new_node.next = current.next
        current.next = new_node

        # Jika node ditambahkan di posisi terakhir,
        # perbarui Tail.
        if new_node.next is None:
            self.tail = new_node

        return new_node

    def insert_at_tail(self, pid, burst_time):
        """Menambahkan proses pada bagian belakang Linked List."""
        new_node = Node(pid, burst_time)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        return new_node

    # ==========================================
    # DELETE OPERATIONS
    # ==========================================

    def delete_at_head(self):
        """Menghapus node pertama Linked List."""

        if self.is_empty():
            return None

        removed_node = self.head
        self.head = self.head.next
        removed_node.next = None

        if self.head is None:
            self.tail = None

        return removed_node

    def delete_at_index(self, index):
        """Menghapus node pada indeks tertentu (0-based)."""

        if index < 0:
            raise IndexError("Index tidak boleh negatif.")

        if self.is_empty():
            raise IndexError("Linked List kosong.")

        if index == 0:
            return self.delete_at_head()

        current = self.head
        position = 0

        # Mencari node sebelum node yang akan dihapus
        while current is not None and position < index - 1:
            current = current.next
            position += 1

        if current is None or current.next is None:
            raise IndexError("Index melebihi panjang Linked List.")

        removed_node = current.next
        current.next = removed_node.next

        # Jika node terakhir dihapus, perbarui Tail
        if removed_node == self.tail:
            self.tail = current

        removed_node.next = None

        return removed_node

    def delete_at_tail(self):
        """Menghapus node terakhir Linked List."""

        if self.is_empty():
            return None

        # Jika hanya terdapat satu node
        if self.head == self.tail:
            removed_node = self.head
            self.head = None
            self.tail = None
            removed_node.next = None
            return removed_node

        current = self.head

        # Mencari node sebelum Tail
        while current.next != self.tail:
            current = current.next

        removed_node = self.tail
        self.tail = current
        self.tail.next = None

        removed_node.next = None

        return removed_node

    # ==========================================
    # ORIGINAL ROUND ROBIN OPERATIONS
    # ==========================================

    def insert_process(self, pid, burst_time):
        """Menambahkan proses baru ke belakang antrean."""
        return self.insert_at_tail(pid, burst_time)

    def enqueue_node(self, node):
        """Memasukkan kembali Node yang sama ke belakang antrean."""
        if node is None:
            return

        node.next = None

        if self.is_empty():
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def dequeue(self):
        """Mengambil dan menghapus proses paling depan."""
        return self.delete_at_head()

    def delete_process(self, pid):
        """Menghapus proses berdasarkan PID."""

        current = self.head
        previous = None

        while current is not None:
            if current.pid == pid:

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current == self.tail:
                    self.tail = previous

                current.next = None
                return True

            previous = current
            current = current.next

        return False

    # ==========================================
    # DISPLAY
    # ==========================================

    def display_processes(self):
        """Menampilkan seluruh proses dalam antrean."""
        current = self.head

        if self.is_empty():
            print("Antrean proses kosong.")
            return

        print("\n=== DAFTAR PROSES CPU ===")
        print("PID\tBurst Time\tRemaining Time")

        while current is not None:
            print(
                f"{current.pid}\t"
                f"{current.burst_time}\t\t"
                f"{current.remaining_time}"
            )
            current = current.next
