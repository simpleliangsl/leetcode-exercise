# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):

        if l1==None and l2==None: return None
        if l1!=None and l2==None: return l1
        if l1==None and l2!=None: return l2

        result = ListNode(0)
        node1 = l1
        node2 = l2
        current = result
        carry = 0
        
        while node1!=None or node2!=None:           
            carry += (node1.val if node1!=None else 0) + \
                     (node2.val if node2!=None else 0)
            
            current.val = carry%10

            if (node1==None or node1.next==None) and \
               (node2==None or node2.next==None) and \
               carry<10:
                break

            carry = carry // 10
            current.next = ListNode(carry)
            
            current = current.next
            node1 = node1.next if node1!=None else None
            node2 = node2.next if node2!=None else None

        return result

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
        
