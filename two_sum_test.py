import unittest
from two_sum import Solution

class SolutionTest(unittest.TestCase):

    # @unittest.skip("temp")
    def test_two_sum_1(self):
        nums = [2,7,11,15]
        target = 9
        result = Solution().twoSum(nums, target)
        self.assertEqual(result, [0,1])

    def test_two_sum_2(self):
        nums = [-3,4,3,90]
        target = 0
        result = Solution().twoSum(nums, target)
        self.assertEqual(result, [0,2])


if __name__ == "__main__":
    unittest.main(verbosity=2)