class Solution:
    """
    @param Matrix: the input
    @return: the element which appears every row
    """
    def FindElements(self, Matrix):
        # write your code here
        result = Matrix[0]
        length = len(Matrix)
        for i in range(1,length):
            for j in result:
                if j not in Matrix[i]:
                    result.remove(j)
        return result[0]
