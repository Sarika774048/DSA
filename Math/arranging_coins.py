# LeetCode 441 - Arranging Coins

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# Example 1:

# Input: n = 5
# Output: 2

class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n >= rows:
            n-=rows
            rows +=1
        return rows -1
