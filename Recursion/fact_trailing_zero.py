# LeetCode 172- Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# Example 1:

# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)
        
