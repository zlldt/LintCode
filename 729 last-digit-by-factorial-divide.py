class Solution:
    """
    @param A: the given number
    @param B: another number
    @return: the last digit of B! / A! 
    """

    def computeLastDigit(self, A, B):
        # write your code here
        factor=1
        value = B
        while value> A:
            factor=((value%10)*factor)%10
            if int(factor)==0:
                return int(factor)
            value-=1
        return int(factor)
