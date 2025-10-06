# LeetCode 242 - Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        for char in t:
            map_t[char] = map_t.get(char, 0) + 1
         
        for key in map_s:
            if map_s[key] != map_t.get(key, 0):
                return False
        return True
