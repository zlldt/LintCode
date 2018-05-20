class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        result = 0
        position = 0
        matrix = 1
        if n>9:
            temp = n%10
            if temp>=8:
                result += matrix
            sum = matrix
            position +=1
            n = n//10
            matrix *= 10
        while n>9:
            temp = n%10
            if temp<8:
                result += sum*temp
            if temp==8:
                result += sum*8+matrix
            if temp==9:
                result += sum*9+matrix
            sum = sum*9 + matrix
            position +=1
            n = n//10
            matrix *= 10
        temp = n%10
        if temp<8:
            result += sum*temp
        else:
            result += sum*8 + matrix
        return result
