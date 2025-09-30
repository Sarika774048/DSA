# Leetcode 67 : Add Binary
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_a = int(a, 2)
        bin_b = int(b, 2)
        result = bin_a + bin_b # integer
        return bin(result)[2:] # excludes first 2 chars
