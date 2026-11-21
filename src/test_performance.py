import random
import time
import tracemalloc
import statistics
import io
from contextlib import redirect_stdout

from round_robin import RoundRobinScheduler


# Konfigurasi pengujian
JUMLAH_PROSES = 1000
TIME_QUANTUM = 4
JUMLAH_PENGUJIAN = 5

# Membuat data burst time yang sama untuk setiap percobaan
rng = random.Random(42)
data_proses = [
    rng.randint(1, 20)
    for _ in range(JUMLAH_PROSES)
]

hasil_waktu = []
hasil_memori = []


for percobaan in range(1, JUMLAH_PENGUJIAN + 1):

    # Membuat scheduler baru
    scheduler = RoundRobinScheduler(quantum=TIME_QUANTUM)

    # Memasukkan 1000 proses
    for i, burst in enumerate(data_proses, start=1):
        scheduler.add_process(f"P{i}", burst)

    # Memulai pengukuran memori
    tracemalloc.start()

    # Mengukur waktu simulasi tanpa output terminal
    output = io.StringIO()

    waktu_awal = time.perf_counter()

    with redirect_stdout(output):
        scheduler.run()

    waktu_akhir = time.perf_counter()

    # Mengambil penggunaan memori puncak
    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    # Konversi waktu ke milidetik
    waktu_ms = (waktu_akhir - waktu_awal) * 1000

    # Konversi memori ke MB
    memori_mb = peak_memory / (1024 * 1024)

    hasil_waktu.append(waktu_ms)
    hasil_memori.append(memori_mb)

    print(f"Pengujian ke-{percobaan}")
    print(f"Waktu eksekusi : {waktu_ms:.4f} ms")
    print(f"Memori puncak  : {memori_mb:.4f} MB")
    print("-" * 40)


# Menghitung rata-rata
rata_waktu = statistics.mean(hasil_waktu)
rata_memori = statistics.mean(hasil_memori)


print("\n=== HASIL RATA-RATA PENGUJIAN ===")
print(f"Jumlah proses    : {JUMLAH_PROSES}")
print(f"Time Quantum    : {TIME_QUANTUM}")
print(f"Jumlah pengujian: {JUMLAH_PENGUJIAN}")
print(f"Rata-rata waktu : {rata_waktu:.4f} ms")
print(f"Rata-rata memori: {rata_memori:.4f} MB")
