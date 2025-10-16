# LeetCode 14 - Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for tup in zip(*strs):
            if len(set(tup)) == 1:
                prefix += tup[0]
            else : break
        return prefix
        
