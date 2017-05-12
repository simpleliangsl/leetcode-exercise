class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: return False
        
        if x == 0: return True

        weight = 10         
        while x/weight >= 1: weight *=  10

        weight /= 10
        while weight > 1:
            a = x//weight
            b = x%10
            if a == b:
                x = (x%weight)//10
                weight = weight//100
            else: return False
            
        return True
