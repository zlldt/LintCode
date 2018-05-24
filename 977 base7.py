class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """
    def convertToBase7(self, num):
        # Write your code here
        tempstr = []
        flag = 0
        if num<0:
            num = -num
            flag=1
        while num>7:
            tempstr.append(str(num%7))
            num = num//7
        if num == 7:
            tempstr.append('0')
            tempstr.append('1')
        else:
            tempstr.append(str(num))
        tempstr.reverse()
        resultstr = ''.join(tempstr)
        if flag == 1:
            resultstr = '-'+resultstr
        return resultstr
