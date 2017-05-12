class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0: return ""

        minLen = min([len(s) for s in strs])

        prefix = strs[0]
        for i in range(minLen):
            for s in strs:
                if s[i] == prefix[i]: continue
                else: return prefix[0:i]

        return prefix[0:minLen]

class Test:
    def testLongestCommonPrefix(self):
        data = ["abc", "abce", "abcef", "abcedfg"]
        expected = "abc"
        actual = Solution().longestCommonPrefix(data)
        assert expected==actual, \
               "[FAILED] expected: {0}, actual: {1}".format(expected, actual)
        print("[PASSED] actual=" + actual + " as expected")
