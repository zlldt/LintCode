class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        if A==[]:
            return 1
        length = len(A)
        for i in range(1,length+1):
            if A.count(i)==0:
                return i
        return length+1
