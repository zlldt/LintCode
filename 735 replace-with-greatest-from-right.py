class Solution:
    """
    @param nums: An array of integers.
    @return: nothing
    """
    def arrayReplaceWithGreatestFromRight(self, nums):
        # Write your code here.
        print(nums)
        length = len(nums)
        temp = nums[length - 1]
        nums[length - 1] = -1
        for i in range(length-2, -1, -1):
            temp, nums[i] = nums[i], temp
            temp = max(nums[i], temp)
        print(nums)

test=Solution()
# test.arrayReplaceWithGreatestFromRight([-1,-1,-1,-1,-1,-1])
test.arrayReplaceWithGreatestFromRight([16,17,4,3,5,2])
