class Solution:
    """
    @param n: an integer
    @return: return an long integer
    """
    def newInteger(self, n):
        # write your code here
        result = 0
        base = 1
        while n>=9:
            result+=(n%9)*base
            n=n//9
            base*=10
        result+=n*base
        return result
