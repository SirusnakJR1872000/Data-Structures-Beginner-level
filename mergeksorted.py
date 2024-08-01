# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# -----------------------------------------------------------------------------------------------------------------------------
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#  1->4->5,
#  1->3->4,
#  2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# -----------------------------------------------------------------------------------------------------------------------------
# Example 2:
# Input: lists = []
# Output: []
# ------------------------------------------------------------------------------------------------------------------------------
# Example 3:
# Input: lists = [[]]
# Output: []
# ------------------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # checking if list is empty
        if not lists or len(lists) == 0:
            return None

        # so if we have more than 1 list we create an empty list
        while len(lists) > 1:
            mergedLists = []

            # now we will iterate through the list in step of 2 i.e we take pair of 2
            # and the loop goes from 0 till the length
            for i in range(0, len(lists), 2):
                # now we retrieve the first list in the pair
                l1 = lists[i]
                # now we retrieve second list if it exists
                l2 = lists[i+1] if (i+1) < len(lists) else None
                # now we call the mergelist method to merge sort both the lists
                mergedLists.append(self.mergelist(l1,l2))
            # now we update the merge lists
            lists = mergedLists
        # now we return the final list
        return lists[0]

    def mergelist(self, l1, l2):
        # lets create a dummy node to handle edge case and tail poimter to keep track of end of list
        dummy = ListNode()
        tail = dummy

        # if l1 and l2 are not None we compare the values
        # the smaller value gets appended to the list
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # now if we have any values left then we just append it to the end of the list
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
        