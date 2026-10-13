import pytest
from lru_cache import LRUCache


def test_put_get():
    c = LRUCache(2)
    c.put("a", 1)
    assert c.get("a") == 1


def test_missing_is_none():
    assert LRUCache(1).get("x") is None


def test_len():
    c = LRUCache(3)
    c.put(1, 1); c.put(2, 2)
    assert len(c) == 2


def test_update_existing_keeps_len():
    c = LRUCache(2)
    c.put("a", 1); c.put("a", 2)
    assert len(c) == 1 and c.get("a") == 2


def test_evicts_least_recently_used():
    c = LRUCache(2)
    c.put("a", 1); c.put("b", 2); c.put("c", 3)
    assert c.get("a") is None and c.get("b") == 2 and c.get("c") == 3


def test_get_refreshes_recency():
    c = LRUCache(2)
    c.put("a", 1); c.put("b", 2)
    c.get("a")
    c.put("c", 3)
    assert c.get("b") is None and c.get("a") == 1


def test_put_refreshes_recency():
    c = LRUCache(2)
    c.put("a", 1); c.put("b", 2)
    c.put("a", 10)
    c.put("c", 3)
    assert c.get("b") is None and c.get("a") == 10


def test_capacity_one():
    c = LRUCache(1)
    c.put("a", 1); c.put("b", 2)
    assert c.get("a") is None and c.get("b") == 2 and len(c) == 1


def test_bad_capacity():
    with pytest.raises(ValueError):
        LRUCache(0)


def test_none_value_is_stored():
    c = LRUCache(2)
    c.put("k", None)
    assert len(c) == 1


def test_many_operations():
    c = LRUCache(100)
    for i in range(1000):
        c.put(i, i * i)
    assert len(c) == 100
    assert c.get(899) is None and c.get(999) == 999 * 999


def test_is_constant_time():
    import time
    small, big = LRUCache(1000), LRUCache(1000)
    for i in range(1000):
        small.put(i, i)
    for i in range(1000):
        big.put(i, i)
    for i in range(1000, 200000):
        big.put(i, i)
    t0 = time.perf_counter(); [small.get(i) for i in range(1000)]; t_small = time.perf_counter() - t0
    t0 = time.perf_counter(); [big.get(i) for i in range(199000, 200000)]; t_big = time.perf_counter() - t0
    assert t_big < 20 * t_small + 0.01
