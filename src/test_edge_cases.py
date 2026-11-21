from round_robin import RoundRobinScheduler


def test_case(judul, daftar_proses):
    print(f"\n{'=' * 45}")
    print(judul)
    print("=" * 45)

    scheduler = RoundRobinScheduler(quantum=4)

    for pid, burst in daftar_proses:
        scheduler.add_process(pid, burst)

    scheduler.run()


# Pengujian 1: Burst Time lebih kecil dari Quantum
test_case(
    "TEST 1: Burst Time < Quantum",
    [("P1", 2)]
)

# Pengujian 2: Burst Time sama dengan Quantum
test_case(
    "TEST 2: Burst Time = Quantum",
    [("P1", 4)]
)

# Pengujian 3: Burst Time lebih besar dari Quantum
test_case(
    "TEST 3: Burst Time > Quantum",
    [("P1", 9)]
)

# Pengujian 4: Antrean kosong
test_case(
    "TEST 4: ANTREAN KOSONG",
    []
)

# Pengujian 5: Beberapa proses dengan durasi berbeda
test_case(
    "TEST 5: MULTIPLE PROCESS",
    [
        ("P1", 10),
        ("P2", 2),
        ("P3", 6),
        ("P4", 1)
    ]
)

print("\n=== SELURUH PENGUJIAN SELESAI ===")