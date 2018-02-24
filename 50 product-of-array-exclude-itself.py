class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        B=[]
        length=len(nums)
        result=1
        if length==1:
            B.append(1)
            return B
        for i in range(1,length):
            result*=nums[i]
        B.append(result)

        for i in range(1,length-1):
            result=1
            for j in range(i):
                result*=nums[j]
            for k in range(i+1,length):
                result*=nums[k]
            B.append(result)
        result=1
        for i in range(0,length-1):
            result*=nums[i]
        B.append(result)
        return B
