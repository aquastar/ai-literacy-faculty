"""Assignment 4: an LRU cache with O(1) get and put.

Fill in the TODOs. You may add helper classes.
"""


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self.capacity = capacity
        # TODO: choose your data structures

    def get(self, key):
        # TODO
        raise NotImplementedError

    def put(self, key, value):
        # TODO
        raise NotImplementedError

    def __len__(self):
        # TODO
        raise NotImplementedError
