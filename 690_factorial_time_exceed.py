class Solution:
    """
    @param n: an integer
    @return:  the factorial of n
    """
    def factorial(self, n):
        # write your code here
        if n == 0:
            return '1'
        resultstr=[]
        temp = n
        while temp>9:
            lastdigit = temp %10
            temp = temp//10
            resultstr.append(str(lastdigit))
        resultstr.append(str(temp))
        numlist = list(resultstr)
        for number in range(2, n):
            length = len(numlist)
            promotion = 0
            for i in range(0, length):
                value = int(numlist[i]) * number + promotion
                if value < 10:
                    numlist[i] = str(value)
                    promotion = 0
                elif value > 9:
                    numlist[i] = (str(value % 10))
                    promotion = value // 10
            if promotion > 0:
                while promotion > 9:
                    numlist.append(str(promotion % 10))
                    promotion = promotion // 10
                numlist.append(str(promotion))
        numlist.reverse()
        resultstr = ''.join(numlist)
        return resultstr
