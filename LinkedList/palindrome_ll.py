# LeetCode 234 - Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return True if arr[::] == arr[::-1] else False
