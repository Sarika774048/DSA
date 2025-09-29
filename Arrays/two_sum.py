# Leetcode 1 - Two sum


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # create a new hashmap
        for i, n in enumerate(nums): # enumerate will returns a (index, value) pair 
            val = target - n   # To find the difference between target and current iterable value
            if val in hashmap:    # if the hashmap comtains the value returns key and current index
                return [hashmap[val], i]  
            else:
                hashmap[n] = i # if val is not in hashmap, adds it in hashmap
