class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        result = ''
        A=ord('A')
        while n>0:
            lower = n%26
            n = n//26
            result = chr(A+lower-1)+result
        return result
