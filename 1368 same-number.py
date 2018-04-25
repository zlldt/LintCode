class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        # Write your code here
        kdict = {}
        for i in range(k):
            if nums[i] in kdict:
                kdict[nums[i]] += 1
            else:
                kdict[nums[i]] = 1
        values = kdict.values()
        if max(values)>1:
            return 'YES'
        length = len(nums)
        for j in range(length-k):
            kdict[nums[j]] -= 1
            if nums[k+j] in kdict:
                kdict[nums[k+j]] += 1
            else:
                kdict[nums[k+j]] = 1
            values = kdict.values()
            if max(values)>1:
                return 'YES'
        return 'NO'
