# LeetCode 414: Third maximum number

# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        distinct = []
        
        for num in nums:
            if num not in distinct:
                distinct.append(num)
            if len(distinct) == 3:
                return distinct[2]

        return distinct[0]
