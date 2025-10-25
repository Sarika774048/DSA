# LeetCode 61 - Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthNode(self, head, k):
        temp = head
        count = 1
        while temp:
            if count == k:
                return temp
            count +=1
            temp = temp.next
        return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k ==0:
            return head
        curr = head
        length = 1 
        tail = curr
        while tail.next:
            length += 1
            tail = tail.next
        if k % length == 0:
            return head
        k = k% length
        tail.next= head
        newTail = self.findNthNode(head, length - k)
        head = newTail.next
        newTail.next = None

        return head

    


       

        
