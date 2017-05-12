class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        haystackList = [i for i in range(len(haystack))]
        needleList = [i for i in range(len(needle))]
        
        for i in haystackList:
            for j in needleList:
                if i+j >= len(haystackList) or haystack[i+j] != needle[j]: break
                if j == len(needleList)-1: return i
        
        return -1;
