# LeetCode 53 - Max SubArray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        summ = largest_sum = nums[0]
        for x in nums[1:n]:
            summ = max(x, summ+x)
            largest_sum = max(summ, largest_sum)
        return largest_sum
        
