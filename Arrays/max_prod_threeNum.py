# LeetCode 628 - Maximum Product of Three Numbers

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

lass Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        result = max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        return result
        
