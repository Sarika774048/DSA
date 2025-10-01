# LeetCode - 125 : Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Time Complexity : O(N)
# Space Complexity : O(N) if we use s1.append -> O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", '').lower()
        s1 = ""

        for char in s:
            if char.isalnum():
                s1 += char
        
        return s1 == s1[::-1]
        
