class Solution:
    """
    @param matrix: an input matrix
    @return: nums[0]: the maximum,nums[1]: the minimum
    """
    def maxAndMin(self, matrix):
        # write your code here
        if matrix == []:
            return []
        nums = [0,0]
        nums[0] = matrix[0][0]
        nums[1] = matrix[0][0]
        length = len(matrix)
        for i in range(length):
            nums[0]=max(nums[0],max(matrix[i]))
            nums[1]=min(nums[1],min(matrix[i]))
        return nums
