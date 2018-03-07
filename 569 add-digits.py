class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
