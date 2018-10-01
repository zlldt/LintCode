class Solution:
    """
    @param matrix: 
    @param x: 
    @param y: 
    @return: return the matrix
    """
    def removeOne(self, matrix, x, y):
        # Write your code here
        matrix[x][y]=0
        height = len(matrix)
        width = len(matrix[0])
        for y in range(1,height):
            for x in range(width):
                if matrix[y][x]==0:
                    continue
                elif matrix[y-1][x]==0:
                    matrix[y][x]=0
        return matrix
