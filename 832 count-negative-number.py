class Solution:
    """
    @param nums: the sorted matrix
    @return: the number of Negative Number
    """
    def countNumber(self, nums):
        # Write your code here
        count = 0
        depth = len(nums)
        width = len(nums[0])
        for i in range(depth):
            if nums[i][0]<0:
                for j in range(width):
                    if nums[i][j]<0:
                        count+=1
        return count
