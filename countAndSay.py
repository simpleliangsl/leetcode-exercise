class Solution:
    # @return a string
    def countAndSay(self, n):
        currentString = "1"
        i = 1
        while i<n:
            char = currentString[0]
            count = 0
            nextString = ""
            for c in currentString:
                if c==char:
                    count += 1
                else:
                    nextString += str(count) + char
                    char = c
                    count = 1
            nextString += str(count) + char
            currentString = nextString
            i += 1
        return currentString

##    # @return a string
##    def countAndSay(self, n):
##        if n == 1:
##            return "1"
##        
##        last = Solution.countAndSay(None, n-1)
##        
##        char = last[0]
##        count = 0
##        current = ""
##        
##        for c in last:
##            if c==char:
##                count += 1
##            else:
##                current += str(count) + char
##                char = c
##                count = 1
##        current += str(count) + char
##        
##        return current
        
