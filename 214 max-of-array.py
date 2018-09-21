class Solution:
    """
    @param A: An integer
    @return: a float number
    """
    def maxOfArray(self, A):
        # write your code here
        result = A[0]
        for a in A:
            result = max(a, result)
        return result
