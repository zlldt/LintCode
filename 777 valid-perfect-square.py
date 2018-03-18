class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        # write your code here
        value = 1
        while num>0:
            num -= value
            value += 2
        if num < 0:
            return False
        return True
