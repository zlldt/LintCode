class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
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
                    resultstr.append('0')
        elif length1 < length2:
            for i in range(minlength, length2):
                if int(numlist2[i]) < 9 and promotion == 1:
                    promotion = 0
                    resultstr.append(str(int(numlist2[i]) + 1))
                elif promotion == 0:
                    resultstr.append(numlist2[i])
                elif int(numlist2[i]) == 9 and promotion == 1:
                    resultstr.append('0')
        if promotion == 1:
            resultstr.append('1')
        resultstr.reverse()
        result = "".join(resultstr)
        return result


    def multiply(self, num1, num2):
        # write your code here
        resultstr = [[] for i in range(0, 10)]
        result = ['' for i in range(0, 10)]
        if num1=='0' or num2=='0':
            return '0'
        numlist1 = list(num1)
        numlist2 = list(num2)
        length1 = len(numlist1)
        length2 = len(numlist2)
        #分解num2，num1作被乘数
        #倒序，高位在后，低位在前
        numlist1.reverse()
        print('numlist1', numlist1)
        print('resultstr', resultstr)
        numlist2.reverse()
        #num1被乘数，乘以1-9，临时结果保存在resultstr中，
        for number in range(1,10):
            promotion = 0
            for i in range(0, length1):
                print('debug:value= ',int(numlist1[i]) * number + promotion)
                value = int(numlist1[i]) * number + promotion
                if value < 10:
                    resultstr[number].append(str(value))
                    promotion = 0
                elif value > 9:
                    resultstr[number].append(str(value % 10))
                    promotion = value // 10
            if promotion > 0:
                resultstr[number].append(str(promotion))
            print('resultstr', resultstr)
        #临时结果resultstr中,乘数为0，结果为0
        resultstr[0] = '0'
        #num2乘数每一位与num1相乘结果查resultstr得出，
        multistr = [[] for i in range(0, length2)]
        multiresult = ['' for i in range(0, length2)]
        for i in range(length2):
            value = int(numlist2[i])
            count = i
            if value > 0:
                while count>0:
                    multistr[i].append('0')
                    count -= 1
                multistr[i].extend(resultstr[value])
        print('multistr:', multistr)

        for i in range(length2):
            multistr[i].reverse()
            multiresult[i] = "".join(multistr[i])
        lastresult=''
        for i in range(length2):
            lastresult = self.addStrings(lastresult,multiresult[i])
        return lastresult
