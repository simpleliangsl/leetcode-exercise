class Solution:
    # @return a string
    def convert(self, s, nRows):

        if s==None or nRows<=0: return None

        if len(s)==0 or nRows==1: return s

        rows = [""] * nRows
        i = 0
        step = 1
        for c in s:
            rows[i] += c
            if i==0: step = 1
            if i==nRows-1: step = -1
            i += step

        result = ""
        for row in rows:
            result += row

        return result
