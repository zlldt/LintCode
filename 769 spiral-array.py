class Solution:
    """
    @param n: a Integer
    @return: a spiral array
    """
    def spiralArray(self, n):
        # write your code here
        result =[[0 for x in range(n)] for y in range(n)]
        number = 1
        max = n*n
        direction = [1,0]
        row=0
        col=0
        result[row][col] = number
        while number < max:
            if (row+direction[0])>=0 and (row+direction[0])<n and (col+direction[1])>=0 and (col+direction[1])<n:
                if result[row+direction[0]][col+direction[1]]==0:
                    number +=1
                    row += direction[0]
                    col += direction[1]
                    result[row][col] = number
                else:
                    direction = self.getNextDirection(direction)
            else:
                direction = self.getNextDirection(direction)
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
