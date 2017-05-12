# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        node1 = l1
        node2 = l2
        current = result
        carry = 0

        while node1 != None or node2 != None:
            if node1 != None:
                carry += node1.val
                node1 = node1.next

            if node2 != None:
                carry += node2.val
                node2 = node2.next

            current.next = ListNode(carry%10)
            current = current.next
            carry = carry // 10

        if carry==1:
            current.next = ListNode(1)

        return result.next

class Test:
    def test_addTwoNumbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        
        current = Solution().addTwoNumbers(l1, l2)

        result = ""
        while current !=None:
            result += str(current.val) + " "
            current = current.next
        print(result)
