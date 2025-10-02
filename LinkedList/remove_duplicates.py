# Leetcode 83 : Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Input: head = [1,1,2]
# Output: [1,2]
# Time Complexity : O(N)
# Space Complexity : O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return  head

 

