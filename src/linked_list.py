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

    def insert_process(self, pid, burst_time):
        """Menambahkan proses baru ke belakang antrean."""
        new_node = Node(pid, burst_time)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

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
        if self.is_empty():
            return None

        removed_node = self.head
        self.head = self.head.next
        removed_node.next = None

        if self.head is None:
            self.tail = None

        return removed_node

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