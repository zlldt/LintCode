class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        length = len(nums)
        if target<nums[0] or target>nums[length-1]:
            return -1
        left, right = 0, length
        while left + 1 < right :
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid
            else :
                right = mid
        if nums[left] == target :
            return left
        elif nums[right] == target :
            return right
        return -1
