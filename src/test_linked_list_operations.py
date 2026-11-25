
from linked_list import SinglyLinkedList


def get_pids(linked_list):
    """Mengambil seluruh PID untuk memeriksa urutan Linked List."""
    result = []
    current = linked_list.head

    while current is not None:
        result.append(current.pid)
        current = current.next

    return result


def create_list():
    """Membuat Linked List berisi P1, P2, P3, P4."""
    linked_list = SinglyLinkedList()

    linked_list.insert_process("P1", 5)
    linked_list.insert_process("P2", 3)
    linked_list.insert_process("P3", 4)
    linked_list.insert_process("P4", 6)

    return linked_list


# ==========================================
# TEST INSERT
# ==========================================

def test_insert_head():
    ll = create_list()
    ll.insert_at_head("P0", 2)

    assert get_pids(ll) == ["P0", "P1", "P2", "P3", "P4"]
    assert ll.head.pid == "P0"

    print("TEST INSERT HEAD: BERHASIL")


def test_insert_middle():
    ll = create_list()
    ll.insert_at_index("PX", 7, 2)

    assert get_pids(ll) == ["P1", "P2", "PX", "P3", "P4"]

    print("TEST INSERT MIDDLE: BERHASIL")


def test_insert_tail():
    ll = create_list()
    ll.insert_at_tail("P5", 8)

    assert get_pids(ll) == ["P1", "P2", "P3", "P4", "P5"]
    assert ll.tail.pid == "P5"

    print("TEST INSERT TAIL: BERHASIL")


def test_insert_empty_list():
    ll = SinglyLinkedList()
    ll.insert_at_head("P1", 5)

    assert get_pids(ll) == ["P1"]
    assert ll.head == ll.tail

    print("TEST INSERT PADA LIST KOSONG: BERHASIL")


def test_insert_at_end_using_index():
    ll = create_list()
    ll.insert_at_index("P5", 8, 4)

    assert get_pids(ll) == ["P1", "P2", "P3", "P4", "P5"]
    assert ll.tail.pid == "P5"

    print("TEST INSERT INDEX TERAKHIR: BERHASIL")


# ==========================================
# TEST DELETE
# ==========================================

def test_delete_head():
    ll = create_list()
    removed = ll.delete_at_head()

    assert removed.pid == "P1"
    assert get_pids(ll) == ["P2", "P3", "P4"]

    print("TEST DELETE HEAD: BERHASIL")


def test_delete_middle():
    ll = create_list()
    removed = ll.delete_at_index(2)

    assert removed.pid == "P3"
    assert get_pids(ll) == ["P1", "P2", "P4"]

    print("TEST DELETE MIDDLE: BERHASIL")


def test_delete_tail():
    ll = create_list()
    removed = ll.delete_at_tail()

    assert removed.pid == "P4"
    assert get_pids(ll) == ["P1", "P2", "P3"]
    assert ll.tail.pid == "P3"

    print("TEST DELETE TAIL: BERHASIL")


def test_delete_single_node():
    ll = SinglyLinkedList()
    ll.insert_process("P1", 5)

    removed = ll.delete_at_tail()

    assert removed.pid == "P1"
    assert ll.head is None
    assert ll.tail is None
    assert ll.is_empty()

    print("TEST DELETE SATU NODE: BERHASIL")


def test_delete_invalid_index():
    ll = create_list()

    try:
        ll.delete_at_index(10)
    except IndexError:
        pass
    else:
        raise AssertionError("Index tidak valid seharusnya menghasilkan IndexError")

    assert get_pids(ll) == ["P1", "P2", "P3", "P4"]

    print("TEST DELETE INDEX INVALID: BERHASIL")


def test_insert_invalid_index():
    ll = create_list()

    try:
        ll.insert_at_index("PX", 7, 10)
    except IndexError:
        pass
    else:
        raise AssertionError("Index tidak valid seharusnya menghasilkan IndexError")

    assert get_pids(ll) == ["P1", "P2", "P3", "P4"]

    print("TEST INSERT INDEX INVALID: BERHASIL")


# ==========================================
# MENJALANKAN SEMUA TEST
# ==========================================

if __name__ == "__main__":
    print("========================================")
    print(" PENGUJIAN LINKED LIST INSERT & DELETE")
    print("========================================\n")

    test_insert_head()
    test_insert_middle()
    test_insert_tail()
    test_insert_empty_list()
    test_insert_at_end_using_index()

    test_delete_head()
    test_delete_middle()
    test_delete_tail()
    test_delete_single_node()
    test_delete_invalid_index()
    test_insert_invalid_index()

    print("\n========================================")
    print(" SEMUA PENGUJIAN SELESAI")
    print("========================================")
