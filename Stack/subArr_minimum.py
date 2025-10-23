# LeetCode 907 - Sum of Subarray Minimums

# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = int(1e9+7)
        nse = self.findNSE(arr)
        pse = self.findPSE(arr)

        total = 0
       

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            total = (total + right * left * arr[i])%mod
        return total

    def findNSE(self, arr):
        n = len(arr)
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            nse[i] = n if not stack else stack[-1]
            stack.append(i)
        return nse

    def findPSE(self, arr):
        n = len(arr)
        pse = [-1] * n
        stack =[]
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            pse[i] = -1 if not stack else stack[-1]
            stack.append(i)
        return pse        
        
