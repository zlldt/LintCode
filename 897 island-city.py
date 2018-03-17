class Solution:
    """
    @param grid: an integer matrix
    @return: an integer
    """

    def numIslandCities(self, grid):
        # Write your code here
        if grid == []:
            return 0
        cityislandcounts = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cityflag = 0
                if grid[i][j] == 2:
                    cityflag = 1
                    self.dfs(i, j, grid, cityflag)
                    cityislandcounts += 1
                if grid[i][j] == 1:
                    cityflag = 0
                    cityflag = self.dfs(i, j, grid, cityflag)
                    if cityflag == 1:
                        cityislandcounts += 1
        return cityislandcounts

    def dfs(self, i, j, grid, cityflag):
        if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])):
            if grid[i][j]:
                if grid[i][j] == 2 and cityflag == 0:
                    cityflag = 1
                grid[i][j] = 0
                cityflag = max(cityflag, self.dfs(i - 1, j, grid, cityflag))
                cityflag = max(cityflag, self.dfs(i + 1, j, grid, cityflag))
                cityflag = max(cityflag, self.dfs(i, j - 1, grid, cityflag))
                cityflag = max(cityflag, self.dfs(i, j + 1, grid, cityflag))
        return cityflag
