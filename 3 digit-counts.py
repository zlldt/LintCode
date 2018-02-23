class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        temp = 0
        count = 0
        for i in range(0, n + 1):
            temp = i
            while temp > 9:
                if (temp % 10 == k):
                    count += 1
                temp //= 10
            if temp == k:
                count += 1
        return count
