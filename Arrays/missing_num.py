# LeetCode 268 - Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        for num in nums:
            summ += num
        actual_sum = sum(list(range(n+1)))
        missing_val = actual_sum - summ
        return missing_val
        
