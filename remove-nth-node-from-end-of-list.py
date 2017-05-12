# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p = head
        
        length = 0
        while p != None:
            length += 1
            p = p.next

        index = length - n - 1
        p = head
        while p != None:
            

        
