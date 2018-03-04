class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        resultstr = []
        numlist1 = list(num1)
        numlist2 = list(num2)
        length1 = len(numlist1)
        length2 = len(numlist2)

        if length1 > length2:
            minlength = length2
        else:
            minlength = length1

        numlist1.reverse()
        numlist2.reverse()
        promotion = 0
        for i in range(0, minlength):
            if int(numlist1[i]) + int(numlist2[i]) + promotion < 10:
                resultstr.append(str(int(numlist1[i]) + int(numlist2[i]) + promotion))
                promotion = 0
            elif int(numlist1[i]) + int(numlist2[i]) + promotion > 9:
                resultstr.append(str((int(numlist1[i]) + int(numlist2[i]) + promotion) % 10))
                promotion = 1

        if length1 > length2:
            for i in range(minlength, length1):
                if int(numlist1[i]) < 9 and promotion == 1:
                    promotion = 0
                    resultstr.append(str(int(numlist1[i]) + 1))
                elif promotion == 0:
                    resultstr.append(numlist1[i])
                elif int(numlist1[i]) == 9 and promotion == 1:
                    promotion = 1
                    resultstr.append('0')
        elif length1 < length2:
            for i in range(minlength, length2):
                if int(numlist2[i]) < 9 and promotion == 1:
                    promotion = 0
                    resultstr.append(str(int(numlist2[i]) + 1))
                elif promotion == 0:
                    resultstr.append(numlist2[i])
                elif int(numlist2[i]) == 9 and promotion == 1:
                    promotion = 1
                    resultstr.append('0')
        if promotion == 1:
            resultstr.append('1')
        resultstr.reverse()
        result = "".join(resultstr)
        return result
