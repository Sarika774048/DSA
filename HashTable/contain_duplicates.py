# Leetcode 217 - Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = 1
        return False
