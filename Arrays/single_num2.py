# LeetCode 137 - Single Number II

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in nums:
            if counter[num] == 1:
                return num
