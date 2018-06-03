class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        length = len(nums)
        numset = set(nums)
        if len(numset)<length:
            return True
        return False
