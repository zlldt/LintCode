class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        length = len(nums)
        count = 0
        while count<(length-count-1):
            nums[count] ^= nums[length-count-1]
            nums[length-count-1] ^= nums[count]
            nums[count] ^= nums[length-count-1]
            count += 1
        return nums
