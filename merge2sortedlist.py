# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

#nMerge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # now we will create a dummy list to handle edge cases
        dummy = ListNode()
        tail = dummy # we will assign the value to tail as it will be used to create a new list by pointing to last node
        
        # now we have to check if list1 and list2 are not None
        while list1 and list2:
            # now comes the comparing part 
            # if element of list 1 is less than element of list 2 the tail pointer will be incremented
            if list1.val < list2.val:
                tail.next = list1
                # now add the element to the tail
                tail = list1
                # now we will move the list pointer to the next node
                list1 = list1.next 
            else:
                # if value of list 2 is less than value of list 1 then the tail pointer is incremented to next value
                tail.next = list2
                # now we will add the value to tail
                tail = list2
                # now we can update the list counter to next node
                list2 = list2.next

        # it might happen that there are some elements left in either list 1 or list 2
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

