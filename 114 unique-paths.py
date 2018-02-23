class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        #path[m][n]={0}
        path=[[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            path[i][0]=1
        for j in range(n):
            path[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                # if i>1 and j>1:
                path[i][j]=path[i-1][j]+path[i][j-1]
        return path[m-1][n-1]
