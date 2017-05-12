class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if A == None: return 0

        newLength = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[newLength] = A[i]
                newLength += 1

        return newLength
