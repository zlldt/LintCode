class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums==[]:
            return []
        length = len(nums)
        result=[]
        value = 0
        for i in range(k):
            value += nums[i]
        result.append(value)
        for j in range(length-k):
            value = value + nums[j+k] - nums[j]
            result.append(value)
        return result
