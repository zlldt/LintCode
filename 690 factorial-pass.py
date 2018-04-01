from functools import reduce  
class Solution:
    """
    @param n: an integer
    @return:  the factorial of n
    """
    def factorial(self, n):
        if n == 0 or n == 1:
            return '1'
        return str(reduce(lambda x,y: x*y, range(1, n+1)))
