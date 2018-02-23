class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def swap(self, A, a, b):
        A[a] ^= A[b]
        A[b] ^= A[a]
        A[a] ^= A[b]

    def partitionArray(self, nums):
        # write your code here
        first = 0
        last = 1
        length = len(nums)
        while last<length-1:
            while (nums[first])%2==1:
                first += 1
            else:
                last = first + 1
                while (nums[last])%2==0:
                    if last==(length-1):
                        return nums
                    last += 1
                else:
                    self.swap(nums,first,last)
                    first += 1
        # return nums 
