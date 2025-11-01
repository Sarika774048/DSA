# LeetCode 47 - Permutataions II 

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(idx, path):
            if idx == len(nums):
                result.append(path[:])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1, path)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0, nums)
        final_result = [list(x) for x in set(tuple(lst) for lst in result)] 
        return final_result
