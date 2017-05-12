class Solution:
    # @return an integer
    def atoi(self, s):
        if len(s) == 0:
            return 0

        numList = []
        hasDigit = False
        for c in s:
            if hasDigit:
                
            if c == "+" or c == "-":
                numlList.append(c)
            elif c >= "0" and c <= "9":
                numlList.apend(c)
                hasDigit = True

        if len(diglList) == 0:
            return 0
        
        sign = sign if sign != None else 1
        result = sign * int("".join(diglList))
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result
