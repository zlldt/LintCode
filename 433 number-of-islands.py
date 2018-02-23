class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid==[]:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res+=1
                    self.dfs(i,j,grid)
        return res

    def dfs(self, i, j, grid):
        if (i>=0 and i <len(grid) and j>=0 and j<len(grid[0])):
            if(grid[i][j]):
                grid[i][j]=0
                self.dfs(i - 1, j, grid)
                self.dfs(i + 1, j, grid)
                self.dfs(i, j - 1, grid)
                self.dfs(i, j + 1, grid)
