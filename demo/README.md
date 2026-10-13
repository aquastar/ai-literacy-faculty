# Assignment 4: LRU cache (data structures)

Implement `LRUCache` in `lru_cache.py`:

- `LRUCache(capacity)`: capacity >= 1
- `get(key)`: return the value, or `None` if absent; marks the key as most recently used
- `put(key, value)`: insert or update; if over capacity, evict the least recently used key
- `__len__()`
- `get` and `put` must be O(1). A dict + doubly linked list is the intended design.

Run the tests with `pytest`. All 12 must pass. Do not modify the tests.
