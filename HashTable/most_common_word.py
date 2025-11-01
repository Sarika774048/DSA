# LeetCode 819 - Most Common Word

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
# Note that words can not contain punctuation symbols.

# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_counter = {}
        banned_words = set(banned)

        normal_str = ''.join(char.lower() if char.isalnum() else ' ' for char in paragraph)

        for word in normal_str.split():
            if word not in banned_words:
                word_counter[word] = word_counter.get(word, 0) + 1
        
        curr_max = 0
        max_word = ''
        for word in word_counter:
            if word_counter[word] > curr_max:
                curr_max = word_counter[word]
                max_word = word
        return max_word       
