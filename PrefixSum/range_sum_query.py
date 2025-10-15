# LeetCode 303 - Range sum query - Immutable

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pref = [0] * (n+1)
        for i in range(n):
            self.pref[i+1] = self.pref[i] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right + 1] - self.pref[left]
        
