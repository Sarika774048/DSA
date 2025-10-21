# LeetCode 32 - Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
  
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlen = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
        return maxlen
