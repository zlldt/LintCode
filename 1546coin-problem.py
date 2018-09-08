class Solution:
    """
    @param n: The guest paid
    @param m: the price
    @return: the sum of the number of banknotes
    """
    def coinProblem(self, n, m):
        # Write your code here
        sum=0
        value = n - m
        changes = [100,50,20,10,5,2,1]
        for change in changes:
            if value >= change:
                sum += value//change
                value = value%change
        return sum
