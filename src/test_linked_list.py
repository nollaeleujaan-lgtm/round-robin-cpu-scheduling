from linked_list import SinglyLinkedList

data_proses = SinglyLinkedList()

# Membuat antrean proses
data_proses.insert_process("P1", 5)
data_proses.insert_process("P2", 3)
data_proses.insert_process("P3", 4)

print("=== ANTREAN AWAL ===")
data_proses.display_processes()

# Mengambil proses P1 dari depan
proses = data_proses.dequeue()

# Simulasi proses P1 telah berjalan selama 3 satuan waktu
proses.remaining_time -= 3

print("\n=== PROSES P1 SETELAH DIJALANKAN ===")
print("PID:", proses.pid)
print("Remaining Time:", proses.remaining_time)

# Memasukkan kembali P1 ke belakang antrean
data_proses.enqueue_node(proses)

print("\n=== ANTREAN SETELAH P1 DIMASUKKAN KEMBALI ===")
data_proses.display_processes()