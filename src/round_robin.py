from linked_list import SinglyLinkedList


class RoundRobinScheduler:
    """
    Scheduler CPU menggunakan algoritma Round Robin.
    """

    def __init__(self, quantum=4):
        self.queue = SinglyLinkedList()
        self.quantum = quantum
        self.current_time = 0
        self.execution_log = []
        self.completion_time = {}

    def add_process(self, pid, burst_time):
        """Menambahkan proses ke antrean scheduler."""
        self.queue.insert_process(pid, burst_time)

    def run(self):
        """Menjalankan seluruh proses menggunakan Round Robin."""

        print("\n=== SIMULASI ROUND ROBIN ===")
        print("Time Quantum:", self.quantum)

        while not self.queue.is_empty():
            process = self.queue.dequeue()

            if process is None:
                break

            # Menentukan lama proses dijalankan
            execution_time = min(
                self.quantum,
                process.remaining_time
            )

            # Mengurangi sisa waktu proses
            process.remaining_time -= execution_time

            # Memperbarui waktu CPU
            self.current_time += execution_time

            # Mencatat proses yang dijalankan
            self.execution_log.append(
                (process.pid, execution_time)
            )

            print(
                f"{process.pid} dijalankan selama "
                f"{execution_time} satuan waktu"
            )

            # Memeriksa apakah proses sudah selesai
            if process.remaining_time == 0:
                self.completion_time[process.pid] = self.current_time
                print(f"{process.pid} selesai.")
            else:
                # Memasukkan kembali proses ke belakang antrean
                self.queue.enqueue_node(process)

        self.display_results()

    def display_results(self):
        """Menampilkan hasil simulasi."""

        print("\n=== URUTAN EKSEKUSI CPU ===")

        for pid, duration in self.execution_log:
            print(f"{pid} -> {duration} satuan waktu")

        print("\n=== WAKTU PENYELESAIAN PROSES ===")

        for pid, time in self.completion_time.items():
            print(f"{pid}: {time}")

        print("\nTotal waktu CPU:", self.current_time)