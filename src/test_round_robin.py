from round_robin import RoundRobinScheduler

# Membuat scheduler dengan Time Quantum 4
scheduler = RoundRobinScheduler(quantum=4)

# Menambahkan proses
scheduler.add_process("P1", 5)
scheduler.add_process("P2", 3)
scheduler.add_process("P3", 4)

# Menampilkan antrean awal
print("=== ANTREAN PROSES ===")
scheduler.queue.display_processes()

# Menjalankan simulasi Round Robin
scheduler.run()