LeetCode 485 - Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_count = 0
        max_count = cur_count

        for num in nums:
            if num == 1:
                cur_count +=1
                max_count = max(cur_count, max_count)
            else: cur_count = 0
        return max_count
