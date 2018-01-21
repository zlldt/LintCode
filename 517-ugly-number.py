#Author: tangwen
#Date: 2018/1/21
class Solution:
    """
    @param: num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num):
        # write your code here
        if num < 1:
            return False
        if num < 5:
            return True;
        while (num % 5 == 0 or num % 3 == 0 or num % 2 == 0):
            if (num % 5 == 0):
                num = num // 5
            elif (num % 3 == 0):
                num = num // 3
            elif (num % 2 == 0):
                num = num // 2
        if(num==1):
            return True
        return False
test=Solution()
print(test.isUgly(6))
