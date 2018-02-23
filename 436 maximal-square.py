class Solution:
    """
    @param: matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        height=len(matrix)
        width=len(matrix[0])
        flag = [[0 for col in range(width)] for row in range(height)]
        maxsize=0
        for x in range(width):
            flag[0][x]=matrix[0][x]
        for y in range(height):
            flag[y][0]=matrix[y][0]
        for y in range(1,height):
            for x in range(1,width):
                if matrix[y][x]==0:
                    flag[y][x]=0
                else:
                    flag[y][x]=1+min(flag[y-1][x],min(flag[y-1][x-1],flag[y][x-1]))

        for x in range(width):
            for y in range(height):
                maxsize=max(maxsize,flag[y][x])
        return maxsize*maxsize
