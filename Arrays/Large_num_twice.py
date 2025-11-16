LeetCode 747 - Largest number at least twice

You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxm = max(nums)
        maxi = nums.index(maxm)
        for i, num in enumerate(nums):
            if i != maxi and maxm < 2* num:
                return -1
        return maxi
