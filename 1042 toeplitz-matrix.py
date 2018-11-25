class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        height = len(matrix)
        width = len(matrix[0])
        for x in range(0, width):
            for y in range(1, height):
                if y+x <= width-1:
                    if not matrix[y][x+y] == matrix[0][x]:
                        return False
        for y in range(1, height):
            for x in range(1, width):
                if x+y <= height-1:
                    if not matrix[y+x][x] == matrix[y][0]:
                        return False
        return True
