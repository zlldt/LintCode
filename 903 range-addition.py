class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        value = 0
        for a,b,x in updates:
            value += x
        result = [value for x in range(length)]

        for start,end,modify in updates:
            if start > 0:
                temp = start -1
                while temp >= 0:
                    result[temp] = result[temp] - modify
                    temp -= 1
            if end < length - 1:
                temp = end + 1
                while temp <= length-1:
                    result[temp] = result[temp] - modify
                    temp += 1
        return result
