class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        start = 1
        sum = 1
        if n==1:
            return 1
        while sum<n:
            start += 1
            sum = start*(1+start)/2
        return start-1
