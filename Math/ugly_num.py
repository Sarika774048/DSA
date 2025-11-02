# LeetCode 263 - Ugly Number

# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.


# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

 class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
        return n  == 1
        
