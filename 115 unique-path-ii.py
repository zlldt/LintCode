class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        path=[[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                path[i][0]=1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                path[0][j]=1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                # if i>1 and j>1:
                if obstacleGrid[i][j]==0:
                    path[i][j]=path[i-1][j]+path[i][j-1]
                else:
                    path[i][j]=0
        return path[m-1][n-1]
