# LeetCode 1480 - Running Sum of 1D Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n)

        for i in range(0, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        return prefix_sum


