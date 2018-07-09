class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    def takeCoins(self, list, k):
        # Write your code here
        result = 0
        length = len(list)
        sum1 = sum(list[0:k])
        result = sum1
        for x in range(k):
            sum1 += - list[k-x-1] + list[-x-1]
            if sum1>result:
                result=sum1
        return result
