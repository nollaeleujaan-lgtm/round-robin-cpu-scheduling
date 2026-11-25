
import unittest
from contextlib import redirect_stdout
from io import StringIO

from round_robin import RoundRobinScheduler


class TestRoundRobinStefanus(unittest.TestCase):

    def setUp(self):
        self.scheduler = RoundRobinScheduler(quantum=4)
        self.scheduler.add_process("P1", 5)
        self.scheduler.add_process("P2", 3)

        # Menyimpan referensi node sebelum simulasi
        self.process_nodes = {}

        current = self.scheduler.queue.head
        while current is not None:
            self.process_nodes[current.pid] = current
            current = current.next

    def run_scheduler_silently(self):
        with redirect_stdout(StringIO()):
            self.scheduler.run()

    # TEST 1: Urutan eksekusi Round Robin
    def test_execution_order(self):
        self.run_scheduler_silently()

        expected = [
            ("P1", 4),
            ("P2", 3),
            ("P1", 1)
        ]

        self.assertEqual(self.scheduler.execution_log, expected)

    # TEST 2: Batas Time Quantum
    def test_time_quantum_limit(self):
        self.run_scheduler_silently()

        for pid, duration in self.scheduler.execution_log:
            self.assertGreater(duration, 0)
            self.assertLessEqual(duration, self.scheduler.quantum)

    # TEST 3: Remaining Time
    def test_remaining_time(self):
        self.run_scheduler_silently()

        self.assertEqual(
            self.process_nodes["P1"].remaining_time, 0
        )
        self.assertEqual(
            self.process_nodes["P2"].remaining_time, 0
        )

    # TEST 4: Completion Time
    def test_completion_time(self):
        self.run_scheduler_silently()

        expected = {
            "P2": 7,
            "P1": 8
        }

        self.assertEqual(self.scheduler.completion_time, expected)

    # TEST 5: Total CPU Time
    def test_total_cpu_time(self):
        self.run_scheduler_silently()

        expected_total = 8

        self.assertEqual(
            self.scheduler.current_time, expected_total
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
