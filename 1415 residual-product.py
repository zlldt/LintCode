class Solution:
    """
    @param arr: The array you should handle
    @return: Return the product
    """
    def getProduct(self, arr):
        # Write your code here
        result = 1
        zeroflag = []
        zerocount = 0
        length = len(arr)
        ans = [0 for x in range(length)]
        if length <2:
            return [0]
        for x in range(length):
            if zerocount>1:
                return ans
            if arr[x] == 0:
                zeroflag.append(x)
                zerocount += 1
            else:
                result *= arr[x]
        if zeroflag == []:
            for x in range(length):
                ans[x]=result//arr[x]
        elif len(zeroflag) == 1:
            for x in zeroflag:
                ans[x]=result
        return ans
