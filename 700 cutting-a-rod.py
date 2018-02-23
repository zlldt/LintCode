class Solution:
    """
    @param prices: the prices
    @param n: the length of rod
    @return: the max value
    """
    def cutting(self, prices, n):
        # Write your code here
        dp=[0 for i in range(n+1)]
        dp[1]=prices[0]
        # print(dp)
        for i in range(2,n+1):
            for j in range(i,0,-1):
                dp[i]=max(dp[i],dp[i-j]+prices[j-1])
            # print(dp)
        return dp[n]
