class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        # Write your code here
        result = 0
        if len(A)==len(B) and len(A)>0:
            for i in range(len(A)):
                result +=A[i]*B[i]
            return result
        else:
            return -1
