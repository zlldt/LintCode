class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        result =[]
        m = len(matrix)
        n = len(matrix[0])
        flag = [[0 for y in range(n)] for x in range(m)]
        direction = [0,1]
        x=0
        y=0
        max = m*n
        number = 1
        result.append(matrix[0][0])
        flag[0][0]=1
        while number < max:
            if (x+direction[0])>=0 and (x+direction[0])<m and (y+direction[1])>=0 and (y+direction[1])<n:
                if flag[x+direction[0]][y+direction[1]]==0:
                    number +=1
                    x += direction[0]
                    y += direction[1]
                    result.append(matrix[x][y])
                else:
                    direction = self.getNextDirection(direction)
            else:
                direction = self.getNextDirection(direction)
        print(result)
        return result

    def getNextDirection(self,direction):
        if direction == [0,1]:
            return [1,0]
        if direction == [1,0]:
            return [0,-1]
        if direction == [0,-1]:
            return [-1,0]
        if direction == [-1,0]:
            return [0,1]

test=Solution()
test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
