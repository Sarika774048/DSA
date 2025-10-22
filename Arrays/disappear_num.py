# LeetCode 448 - Find all numbers disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full_set = set(range(1, n+1))
        num_set = set(nums)
        disappeared_nums = list(full_set - num_set)
        return disappeared_nums
