
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        i = 0
        d = {}
        maxLength = 0
        
        while i < len(s):
            if s[i] in d:
                maxLength = max(len(d), maxLength)
                i = d[s[i]]
                d.clear()
            else:
                d[s[i]] = i
                
            i += 1

        return max(len(d), maxLength)

import timeit
class Test:
    def testLengthOfLongestSubstring(self):
        stmt = "Solution().lengthOfLongestSubstring('abc')"
        setup = "from __main__ import Solution"
        print(timeit.timeit(stmt, setup, number=1))
