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
        sum1 = 0
        tailnumber = 0
        if n>9:
            temp = n % 10
            if temp >= 8:
                result += matrix
            sum1 = matrix
            tailnumber += temp
            position += 1
            n = n//10
            matrix *= 10
        while n > 9:
            temp = n % 10
            if temp < 8:
                result += sum1*temp
            if temp == 8:
                result += sum1*8+matrix
            if temp == 9:
                result += sum1*9+matrix
            sum1 = sum1*9 + matrix
            tailnumber += temp*matrix
            position += 1
            n = n//10
            matrix *= 10
        temp = n % 10
        if temp < 8:
            result += sum1*temp
        elif temp == 8:
            result = sum1*8 + tailnumber + 1
        elif temp == 9:
            result += sum1*8 + matrix
        return result
