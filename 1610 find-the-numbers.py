class Solution:
    """
    @param n: the integer
    @return: the numbers that larger and smaller than `n` 
    """
    def getNumbers(self, n):
        # Write your code here
        if n<0:
            return []
        elif n==0:
            return [1]
        min,mid,max = 0,1,1
        while min<n and mid<n:
            min,mid,max = mid,max,max+mid
        if mid>n:
            return [min,mid]
        else:
            return [min,max]
