class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if target not in nums:
            return -1
        length = len(nums)
        start, end = 0, len(nums)-1
        while start +1 < end:
            mid = (start + end)//2
            if target < nums[mid]:
                end = mid
            else:
                start = mid
        if nums[end]== target:
            return end
        elif nums[start]== target:
            return start
