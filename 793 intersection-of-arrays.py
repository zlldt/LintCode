class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        length = len(arrs)
        result = self.intersection(arrs[0], arrs[1])
        for i in range(2,length):
            result = self.intersection(result, arrs[i])
        return len(result)
        
    def intersection(self, arr1, arr2):
        result = []
        for item in arr1:
            if item in arr2:
                result.append(item)
        return result
