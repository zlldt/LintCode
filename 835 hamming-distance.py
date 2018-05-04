class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        count = 0
        value = x^y
        while value > 0:
            count += value % 2
            value = value // 2
        return count
