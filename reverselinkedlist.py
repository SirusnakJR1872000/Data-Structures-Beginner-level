# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 # Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we will initialize prev to None as there is no previous node to the head 
        # and curr will be the head
        prev, curr = None, head
        # now we will iterate through the loop till curr is not None
        while curr:
            # now we need to preserve the reference to the list before changing to next pointer of current node
            nxt = curr.next
            # now we need to reverse the direction of the list by pointing the next of current node to previous
            curr.next = prev
            # now we will move the prev to next node
            prev = curr
            # now we will move the curr node
            curr = nxt 
        # after the loop is done we will return prev which will contain new head of the reversed list
        return prev
