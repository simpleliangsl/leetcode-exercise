# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):

        current = head = ListNode(0)

        while l1 != None or l2 != None:
            
            temp = None
            if l1 == None: temp = l2.val
            elif l2 == None: temp = l1.val
            else: temp = min(l1.val, l2.val)

            
            current.next = ListNode(temp)
            current = current.next

            if l1 != None and l1.val == temp: l1 = l1.next
            elif l2 != None and l2.val == temp: l2 = l2.next
        
        return head.next
        
