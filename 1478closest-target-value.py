class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        # Write your code here
        length = len(array)
        array = sorted(array)
        sum = array[0]+array[1]
        if sum>target:
            return -1
        for x in range(length-1):
            for y in range(x+1,length):
                if array[x]+array[y]>sum and array[x]+array[y]<=target:
                    sum=array[x]+array[y]
                if sum==target:
                    return target
        return sum
