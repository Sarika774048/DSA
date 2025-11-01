# LeetCode 46 - Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        return result

