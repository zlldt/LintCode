class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        length = len(A)
        if length == 0:
            return 0
        if target<A[0]:
            return 0
        if target>A[length-1]:
            return length
        left, right = 0, length
        while left + 1 < right :
            mid = (left + right) // 2
            if A[mid] < target :
                left = mid
            else :
                right = mid
        if A[left] == target :
            return left
        elif A[right] == target :
            return right
        elif target<A[left] :
            return left
        elif target>A[right] :
            return right+1
        else :
            return right
        return 0
