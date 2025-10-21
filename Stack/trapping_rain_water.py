# LeetCode 42 - Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = rmax = total = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] < lmax:
                    total += lmax - height[left]
                else:
                    lmax = height[left]
                left = left+1
            else:
                if height[right] < rmax:
                    total += rmax - height[right]
                else:
                    rmax = height[right]
                right = right-1
        return total
