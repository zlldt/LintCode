#Author: zlldt
#Date: 2018/2/26
class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        # write your code here
        value = [1 for i in range(n+1)]
        value[0] = 0
        value[1] = 0
        temp = 0
        for i in range(2, (n+1)//2):
            temp = i * 2
            if temp > n:
                break
            while temp < n:
                value[temp] = 0
                temp += i
        return value.count(1)
