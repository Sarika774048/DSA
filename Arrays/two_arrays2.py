# LeetCode 350 - Intersection of Array 2
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        new_list = []

        for num in nums2:
            if count[num] > 0:
                new_list.append(num)
                count[num] -= 1

        return new_list
        
