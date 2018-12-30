class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        height = len(grid)
        width = len(grid[0])
        landcount = 0
        connected = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x]==1:
                    landcount+=1
                    if y>=1:
                        if grid[y-1][x]==1:
                            connected+=1
                    if y<=(height-2):
                        if grid[y+1][x]==1:
                            connected+=1
                    if x>=1:
                        if grid[y][x-1]==1:
                            connected+=1
                    if x<=(width-2):
                        if grid[y][x+1]==1:
                            connected+=1
        return landcount*4-connected    
