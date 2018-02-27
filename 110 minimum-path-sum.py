class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if grid == []:
            return 0
        height = len(grid)
        width = len(grid[0])
        
        path=[[0 for col in range(width)] for row in range(height)]
        path[0][0] = grid[0][0]
        for i in range(1, height):
            path[i][0] = path[i-1][0]+grid[i][0]
        for j in range(1, width):
            path[0][j] = path[0][j-1]+grid[0][j]
        for i in range(1,height):
            for j in range(1,width):
                path[i][j]=min(path[i-1][j],path[i][j-1])+grid[i][j]
        return path[height-1][width-1]
        
        # for i in range(1, height):
        #     grid[i][0] = grid[i-1][0]+grid[i][0]
        # for j in range(1, width):
        #     grid[0][j] = grid[0][j-1]+grid[0][j]
        # for i in range(1,height):
        #     for j in range(1,width):
        #         grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        # return grid[height-1][width-1]
