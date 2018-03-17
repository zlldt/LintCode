class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        # Write your code here
        length = len(arr)
        width = len(arr[0])
        min = width
        for i in range(length):
            for j in range(width):
                if arr[i][j]==1:
                    if j < min:
                        min = j
                    continue
            if min == 0:
                return min
        return min
