
from linked_list import SinglyLinkedList


def test_insert_process():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)
    queue.insert_process("P2", 3)

    assert queue.head.pid == "P1"
    assert queue.tail.pid == "P2"
    assert queue.head.next.pid == "P2"
    assert queue.tail.next is None

    print("TEST INSERT: BERHASIL")


def test_dequeue():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)
    queue.insert_process("P2", 3)

    removed = queue.dequeue()

    assert removed.pid == "P1"
    assert queue.head.pid == "P2"
    assert queue.tail.pid == "P2"
    assert removed.next is None

    print("TEST DEQUEUE: BERHASIL")


def test_dequeue_empty():
    queue = SinglyLinkedList()

    removed = queue.dequeue()

    assert removed is None
    assert queue.head is None
    assert queue.tail is None

    print("TEST DEQUEUE KOSONG: BERHASIL")


def test_delete_middle():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)
    queue.insert_process("P2", 3)
    queue.insert_process("P3", 7)

    result = queue.delete_process("P2")

    assert result is True
    assert queue.head.pid == "P1"
    assert queue.head.next.pid == "P3"
    assert queue.tail.pid == "P3"
    assert queue.tail.next is None

    print("TEST DELETE NODE TENGAH: BERHASIL")


def test_delete_head():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)
    queue.insert_process("P2", 3)

    result = queue.delete_process("P1")

    assert result is True
    assert queue.head.pid == "P2"
    assert queue.tail.pid == "P2"

    print("TEST DELETE HEAD: BERHASIL")


def test_delete_tail():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)
    queue.insert_process("P2", 3)

    result = queue.delete_process("P2")

    assert result is True
    assert queue.head.pid == "P1"
    assert queue.tail.pid == "P1"
    assert queue.tail.next is None

    print("TEST DELETE TAIL: BERHASIL")


def test_delete_not_found():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)

    result = queue.delete_process("P9")

    assert result is False
    assert queue.head.pid == "P1"
    assert queue.tail.pid == "P1"

    print("TEST PID TIDAK DITEMUKAN: BERHASIL")


def test_delete_last_node():
    queue = SinglyLinkedList()

    queue.insert_process("P1", 5)

    result = queue.delete_process("P1")

    assert result is True
    assert queue.head is None
    assert queue.tail is None
    assert queue.is_empty() is True

    print("TEST DELETE NODE TERAKHIR: BERHASIL")


if __name__ == "__main__":
    test_insert_process()
    test_dequeue()
    test_dequeue_empty()
    test_delete_middle()
    test_delete_head()
    test_delete_tail()
    test_delete_not_found()
    test_delete_last_node()

    print("\nSEMUA PENGUJIAN MARIA SELESAI.")
