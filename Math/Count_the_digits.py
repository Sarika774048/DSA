# LeetCode 2520 - Count the Digits that divide a Number

# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

# Example 1:

# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.

class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        original_num = num  # Keep the original number for divisibility check
        
        while num > 0:
            digit = num % 10
            num = num // 10
            if digit != 0 and original_num % digit == 0:
                count += 1
        
        return count
