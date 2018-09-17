class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if L==[]:
            return 0
        right = max(L)
        left = 1
        while left+1 < right:
            maxlength = (left +right) // 2
            count = 0
            for woodlength in L:
                count += woodlength//maxlength
            if count < k:
                # print('count<k',count, maxlength, left, right)
                right = maxlength
            elif count >= k:
                # print('count>k',count, maxlength, left, right)
                left = maxlength
        # print(count)

        count = 0
        for woodlength in L:
            count += woodlength//left
        if count >=k:
            return left
        count = 0
        for woodlength in L:
            count += woodlength//right
        if count >=k:
            return right
        return 0
