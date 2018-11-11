class Solution:
    """
    @param x: an array of n positive numbers
    @return: determine if your path crosses itself
    """
    def isSelfCrossing(self, x):
        # write your code here
        if x[0]>=x[2] and x[1]<=x[3]:
            return True
        return False
