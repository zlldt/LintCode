class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        # Write your code here
        length = len(nums)
        result = [0 for x in range(length - k + 1)]
        for x in range(k):
            result[0]+=nums[x]
        for y in range(1,length-k+1):
            result[y]=result[y-1]-nums[y-1]+nums[y+k-1]
        return max(result)/k
