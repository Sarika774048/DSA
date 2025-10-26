# LeetCode 1390 - Four Divisors

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for n in nums:
            divisors = []
        
            for i in range(1, int(n ** 0.5) +1):
                if n % i ==0:
                    divisors.append(i)
                    if i != n //i:
                        divisors.append( n//i)
            if len(divisors) == 4:
                total += sum(divisors)
        return total
