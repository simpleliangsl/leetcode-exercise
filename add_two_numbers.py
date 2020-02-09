'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

https://leetcode-cn.com/problems/add-two-numbers
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = None
        current = None
        prev = None
        carry = 0

        while l1 != None or l2 != None or carry > 0:

            val1 = 0
            if l1 != None:
                val1 = l1.val
                l1 = l1.next
            
            val2 = 0
            if l2 != None:
                val2 = l2.val
                l2 = l2.next

            sum_val = (val1 + val2 + carry)
            val = sum_val
            carry = 0

            if sum_val >= 10:
                val = sum_val - 10
                carry = 1

            current = ListNode(val)

            if head == None:
                head = current

            if prev != None:
                prev.next = current

            prev = current
        
        return head
                