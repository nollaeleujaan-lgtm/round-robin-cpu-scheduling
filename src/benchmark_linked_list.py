
import csv
import time
import statistics
import gc
import matplotlib.pyplot as plt

from linked_list import SinglyLinkedList


# ============================================================
# KONFIGURASI BENCHMARK
# ============================================================

DATA_SIZES = [100, 1000, 10000, 100000]
REPEAT = 50
WARMUP = 3

RESULT_FILE = "benchmark_results_v3.csv"

INSERT_GRAPH_FILE = "grafik_benchmark_insert_v3.png"
DELETE_GRAPH_FILE = "grafik_benchmark_delete_v3.png"


# ============================================================
# MEMBUAT LINKED LIST
# ============================================================

def create_linked_list(size):
    linked_list = SinglyLinkedList()

    for i in range(size):
        linked_list.insert_at_tail(f"P{i}", 10)

    return linked_list


# ============================================================
# MENENTUKAN OPERASI YANG DIUJI
# ============================================================

def prepare_operation(operation, linked_list, size):

    if operation == "Insert Head":
        return lambda: linked_list.insert_at_head("NEW", 10)

    elif operation == "Insert Middle":
        return lambda: linked_list.insert_at_index(
            "NEW", 10, size // 2
        )

    elif operation == "Insert Tail":
        return lambda: linked_list.insert_at_tail("NEW", 10)

    elif operation == "Delete Head":
        return lambda: linked_list.delete_at_head()

    elif operation == "Delete Middle":
        return lambda: linked_list.delete_at_index(size // 2)

    elif operation == "Delete Tail":
        return lambda: linked_list.delete_at_tail()

    else:
        raise ValueError(f"Operasi tidak dikenal: {operation}")


# ============================================================
# WARM-UP
# ============================================================

def warm_up(operation, size):

    for _ in range(WARMUP):
        linked_list = create_linked_list(size)
        action = prepare_operation(operation, linked_list, size)
        action()


# ============================================================
# MENGUKUR WAKTU OPERASI
# ============================================================

def measure_operation(operation, size):

    times = []

    # Warm-up sebelum pengukuran
    warm_up(operation, size)

    # Bersihkan garbage sebelum memulai pengukuran
    gc.collect()

    for _ in range(REPEAT):

        # Persiapan struktur data di luar timer
        linked_list = create_linked_list(size)
        action = prepare_operation(operation, linked_list, size)

        # Simpan kondisi Garbage Collection
        gc_was_enabled = gc.isenabled()

        # Nonaktifkan GC hanya saat operasi diukur
        if gc_was_enabled:
            gc.disable()

        try:
            start = time.perf_counter_ns()
            action()
            end = time.perf_counter_ns()

        finally:
            # Pulihkan kondisi GC
            if gc_was_enabled:
                gc.enable()

        elapsed_us = (end - start) / 1000
        times.append(elapsed_us)

    average = statistics.mean(times)
    median = statistics.median(times)

    return average, median


# ============================================================
# MEMBUAT GRAFIK BENCHMARK
# ============================================================

def create_graphs(results):

    sizes = DATA_SIZES

    insert_operations = [
        "Insert Head",
        "Insert Middle",
        "Insert Tail"
    ]

    delete_operations = [
        "Delete Head",
        "Delete Middle",
        "Delete Tail"
    ]

    # Data median untuk grafik
    median_data = {}

    for item in results:
        key = (item["Data Size"], item["Operation"])
        median_data[key] = item["Median (us)"]

    # --------------------------------------------------------
    # GRAFIK INSERT
    # --------------------------------------------------------

    plt.figure(figsize=(10, 6))

    for operation in insert_operations:

        values = [
            median_data[(size, operation)]
            for size in sizes
        ]

        plt.plot(
            sizes,
            values,
            marker="o",
            linewidth=2,
            label=operation
        )

    plt.xscale("log")
    plt.yscale("log")

    plt.xticks(
        sizes,
        ["100", "1.000", "10.000", "100.000"]
    )

    plt.title("Benchmark Operasi Insert - Singly Linked List")
    plt.xlabel("Jumlah Node")
    plt.ylabel("Waktu Eksekusi (µs)")

    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    plt.savefig(INSERT_GRAPH_FILE, dpi=300, bbox_inches="tight")

    print(f"Grafik Insert tersimpan: {INSERT_GRAPH_FILE}")

    plt.show()


    # --------------------------------------------------------
    # GRAFIK DELETE
    # --------------------------------------------------------

    plt.figure(figsize=(10, 6))

    for operation in delete_operations:

        values = [
            median_data[(size, operation)]
            for size in sizes
        ]

        plt.plot(
            sizes,
            values,
            marker="o",
            linewidth=2,
            label=operation
        )

    plt.xscale("log")
    plt.yscale("log")

    plt.xticks(
        sizes,
        ["100", "1.000", "10.000", "100.000"]
    )

    plt.title("Benchmark Operasi Delete - Singly Linked List")
    plt.xlabel("Jumlah Node")
    plt.ylabel("Waktu Eksekusi (µs)")

    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    plt.savefig(DELETE_GRAPH_FILE, dpi=300, bbox_inches="tight")

    print(f"Grafik Delete tersimpan: {DELETE_GRAPH_FILE}")

    plt.show()


# ============================================================
# BENCHMARK UTAMA
# ============================================================

def run_benchmark():

    operations = [
        "Insert Head",
        "Insert Middle",
        "Insert Tail",
        "Delete Head",
        "Delete Middle",
        "Delete Tail"
    ]

    results = []

    print("=" * 80)
    print(" BENCHMARK SINGLY LINKED LIST - VERSI 3")
    print("=" * 80)
    print(f"Warm-up             : {WARMUP} kali")
    print(f"Pengukuran          : {REPEAT} kali")
    print("Nilai utama         : Median")
    print("GC                 : Dinonaktifkan saat timer operasi")
    print("Satuan              : Mikrodetik (us)")
    print("-" * 80)

    for size in DATA_SIZES:

        print(f"\nJumlah Data: {size}")

        for operation in operations:

            average, median = measure_operation(operation, size)

            results.append({
                "Data Size": size,
                "Operation": operation,
                "Average (us)": round(average, 4),
                "Median (us)": round(median, 4)
            })

            print(
                f"{operation:<18} | "
                f"Median: {median:>10.4f} us | "
                f"Rata-rata: {average:>10.4f} us"
            )

    # --------------------------------------------------------
    # MENYIMPAN HASIL CSV
    # --------------------------------------------------------

    with open(
        RESULT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "Data Size",
            "Operation",
            "Average (us)",
            "Median (us)"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    print("\n" + "=" * 80)
    print("BENCHMARK VERSI 3 SELESAI")
    print(f"Jumlah skenario: {len(results)}")
    print(f"Hasil CSV tersimpan: {RESULT_FILE}")
    print("=" * 80)

    # Membuat grafik secara otomatis
    create_graphs(results)


# ============================================================
# PROGRAM UTAMA
# ============================================================

if __name__ == "__main__":
    run_benchmark()
