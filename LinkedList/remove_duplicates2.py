# LeetCode 82 - Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate_val = curr.val
                # skip the entire group
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next

        return dummy.next
