from typing import Self
from Q1.classes.Product import Product


class HashTable:
    class BucketEntry:
        """Linked list implementation."""

        def __init__(self, key: str, value: Product, next: Self | None = None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, capacity=10):
        self.buckets: list[HashTable.BucketEntry | None] = [None] * capacity
        self.bucket_tails: list[HashTable.BucketEntry | None] = [None] * capacity
        self.capacity = capacity

    def _hash(self, key: str) -> int:
        """Horner's method for hashing."""
        hash_value = 0
        for i, char in enumerate(key):
            hash_value += ord(char) * (i + 1)
        return hash_value % self.capacity

    def insert(self, key: str, value: Product):
        new_entry = self.BucketEntry(key=key, value=value)

        hash_index = self._hash(key)
        tail = self.bucket_tails[hash_index]

        if tail is None:
            self.buckets[hash_index] = new_entry
        else:
            tail.next = new_entry
        self.bucket_tails[hash_index] = new_entry

    def search(self, key: str):
        bucket = self.buckets[self._hash(key)]

        current_entry = bucket
        while current_entry:
            if current_entry.key == key:
                return current_entry
            current_entry = current_entry.next

        return None

    def print(self):
        line = ""
        for i, bucket in enumerate(self.buckets):
            line += f"[{i}] "

            if not bucket:
                line += "None\n"
                continue

            current_entry = bucket
            while current_entry:
                line += f"({current_entry.key}, {current_entry.value}) -> "
                current_entry = current_entry.next
            line += "\n"

        print(line)
