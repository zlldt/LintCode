class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix ==[]:
            return False
        linenumber = 0
        height = len(matrix)
        width = len(matrix[0])
        if target < matrix[0][0] or target > matrix[height-1][width-1]:
            return False
        col0 = []
        for i in range(height):
            col0.append(matrix[i][0])
        found,linenumber = self.bin_search(col0,target)
        if found == True:
            return True
        found,_ = self.bin_search(matrix[linenumber],target)
        return found

    def bin_search(self, data_list, target):
        low, high = 0, len(data_list)-1
        while low + 1 < high:
            mid = (low + high) // 2
            if data_list[mid] < target:
                low = mid
            else:
                high = mid
        if data_list[low] == target or data_list[high] == target:
            return True, 0
        elif data_list[high] < target:
            return False, high
        elif data_list[low] < target:
            return False, low
