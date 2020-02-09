import unittest
from longest_substring import Solution

class SolutionTest(unittest.TestCase):

    def test_length_of_longest_substring_1(self):
        result = Solution().lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(result, 3)

    def test_length_of_longest_substring_2(self):
        result = Solution().lengthOfLongestSubstring("bbbbb")
        self.assertEqual(result, 1)

    def test_length_of_longest_substring_3(self):
        result = Solution().lengthOfLongestSubstring("pwwkew")
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)