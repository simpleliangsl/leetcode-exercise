import unittest
from add_two_numbers import Solution
from add_two_numbers import ListNode

class SolutionTest(unittest.TestCase):

    @staticmethod
    def create_nodes(*nums):

        head = None
        current = None
        prev = None

        for i in nums:
            current = ListNode(i)

            if head == None:
                head = current
            
            if prev != None:
                prev.next = current
            
            prev = current
        
        return head

    @staticmethod
    def to_list(l: ListNode):
        result = []
        while l != None:
            result.append(l.val)
            l = l.next
        return result

    def test_add_two_numbers_1(self):
        l1 = SolutionTest.create_nodes(2, 4, 3)
        l2 = SolutionTest.create_nodes(5, 6, 4)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(SolutionTest.to_list(result), [7, 0, 8])

    def test_add_two_numbers_2(self):
        l1 = SolutionTest.create_nodes(5)
        l2 = SolutionTest.create_nodes(5)
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(SolutionTest.to_list(result), [0, 1])

if __name__ == "__main__":
    unittest.main(verbosity=2)