class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        # Write your code here
        resultA=self.getResult(inputA)
        resultB=self.getResult(inputB)

        lengthA = len(resultA)
        lengthB = len(resultB)
        if not lengthA == lengthB:
            return 'NO'
        if resultA==[] and resultB==[]:
            return 'YES'
        for i in range(lengthA):
            if not resultA[i] == resultB[i]:
                return 'NO'
        return 'YES'

    def getResult(self, input):
        result=[]
        for i in input:
            if i=='<':
                if len(result)>0:
                    result.pop()
            else:
                result.append(i)
        return result
