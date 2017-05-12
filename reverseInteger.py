import time

class Solution:
    # @return an integer
    def reverse(self, x):
        xString = str(x)
        isNegative = xString[0]=="-"
        
        result = []
        if isNegative:
            result.append("-");
      
        for i in range(len(xString)-1, 0 if isNegative else -1, -1):
            result.append(xString[i])

        resultInt =  int("".join(result))   
        return resultInt if resultInt <= 2147483647 and resultInt >=-2147483648 else 0


class SolutionTest:
    def testReverse(self):
        solution = Solution()
        startClock = time.clock()
        solution.reverse(2147483647)
        print("time elapsed: " + str(time.clock() - startClock))
