import math
class Solution:
    """
    @param num: an integer
    @return: returns true when it is a perfect number and false when it is not
    """
    def checkPerfectNumber(self, num):
        # write your code here
        sum1=1
        if num<6:
            return False
        for x in range(2, int(math.sqrt(num))+1):
            if num%x==0 and x*x<num:
                sum1+=x+num//x
        if sum1==num:
            return True
        return False
