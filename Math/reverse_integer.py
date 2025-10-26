# LeetCode 7 - Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse_num = 0
        while x > 0:
            last_digit = x % 10
            x = x // 10
            reverse_num = reverse_num * 10 + last_digit

        reverse_num *= sign

        if  reverse_num< -2**31 or reverse_num > 2**31:
            return 0
        
        return reverse_num
