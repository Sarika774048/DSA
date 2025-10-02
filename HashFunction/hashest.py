# LeetCode 705 - Design HashSet

# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
    
    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.hash(key)
        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            if key not in self.table[hv]:
                self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.hash(key)
        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        hv = self.hash(key)
        if self.table[hv] != None:
            return key in self.table[hv]
        return False
