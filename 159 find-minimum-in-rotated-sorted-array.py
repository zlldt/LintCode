class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        length = len(nums)
        if length>=2:
            if nums[0]<nums[length-1]:
                return nums[0]
            else:
                value = min(self.findMin(nums[:length // 2]), self.findMin(nums[length // 2:]))
                return value
        if length == 2:
            return min(nums[0],nums[1])
        return nums[0]
