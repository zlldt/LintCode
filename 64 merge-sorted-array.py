class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        C = []
        i = 0
        j = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        if i == m:
            temp = B[j:n]
            C = C + temp
        elif j == n:
            temp = A[i:m]
            C = C + temp
        for x in range(m+n):
            A[x] = C[x]
        A = A + C[m:m+n]
