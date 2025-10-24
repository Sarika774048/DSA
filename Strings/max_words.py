# LeetCode 2114 - Maximum Number of Words in a Sentence

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

# Example 1:

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum_number = 0
        for sentence in sentences:
            words = sentence.split()
            maximum_number = max(maximum_number, len(words))
        
        return maximum_number
