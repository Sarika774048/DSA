# Leetocode 11 - Containter with most water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxarea = 0
    
        while l < r:
            w = r-l
            h = min(height[l], height[r])
            a = w*h
            maxarea = max(maxarea, a)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return maxarea
                
