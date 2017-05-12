class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numDict = {}
        
        # make a dictionary in which each pair is (value, index) from num list
        for index, value in enumerate(num):
            numDict[value] = [index+1] if value not in numDict else numDict[value]+[index+1]
            
        # foreach n in num, if m=target-n exists, then return indexs of n and m     
        for n in num:
            m = target-n
            if n == m and len(numDict[n]) >= 2:
                return numDict[n][0], numDict[m][1]
            elif n != m and m in numDict:
                return numDict[n][0], numDict[m][0]

        # No result
        return None
