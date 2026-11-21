
from round_robin import RoundRobinScheduler


def main():
    print("=" * 40)
    print(" SIMULASI CPU ROUND ROBIN SCHEDULING")
    print("=" * 40)

    # Memasukkan Time Quantum
    while True:
        try:
            quantum = int(input("Masukkan Time Quantum: "))

            if quantum <= 0:
                print("Time Quantum harus lebih dari 0.")
                continue

            break

        except ValueError:
            print("Masukkan angka yang valid.")

    # Membuat scheduler
    scheduler = RoundRobinScheduler(quantum=quantum)

    # Memasukkan jumlah proses
    while True:
        try:
            jumlah_proses = int(input("Masukkan jumlah proses: "))

            if jumlah_proses <= 0:
                print("Jumlah proses harus lebih dari 0.")
                continue

            break

        except ValueError:
            print("Masukkan angka yang valid.")

    # Memasukkan Burst Time setiap proses
    print("\n=== INPUT BURST TIME ===")

    for i in range(1, jumlah_proses + 1):
        while True:
            try:
                burst_time = int(
                    input(f"Masukkan Burst Time P{i}: ")
                )

                if burst_time <= 0:
                    print("Burst Time harus lebih dari 0.")
                    continue

                scheduler.add_process(
                    f"P{i}",
                    burst_time
                )

                break

            except ValueError:
                print("Masukkan angka yang valid.")

    # Menampilkan antrean awal
    print("\n=== ANTREAN PROSES ===")
    scheduler.queue.display_processes()

    # Menjalankan simulasi
    scheduler.run()


if __name__ == "__main__":
    main()
