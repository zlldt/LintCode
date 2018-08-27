class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
def getRow(self, rowIndex):
    # write your code here
    firstrow=[1,1]
    if rowIndex==1:
        return [1,1]
    for x in range(2,rowIndex+1):
        newrow = [1]
        for index in range(1,x):
            newrow.append(firstrow[index]+firstrow[index-1])
        newrow.append(1)
        firstrow=newrow
    return firstrow
