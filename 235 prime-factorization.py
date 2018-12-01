import math
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        result = []
        maxvalue = int(math.sqrt(num))+1
        for x in range(2,maxvalue):
            while num%x==0:
                result.append(x)
                num = num//x
        if num>1:
            result.append(num)
        return result
