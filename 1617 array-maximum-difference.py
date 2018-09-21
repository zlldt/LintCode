class Solution:
    """
    @param a: the array a
    @return: return the maximum value
    """
    def getAnswer(self, a):
        # Write your code here
        length = len(a)
        result = 0
        for item in a:
            if item%2==1:
                minimal = item
                break
        for item in a:
            if item%2==1:
                if item<minimal:
                    minimal = item
            else:
                if item-minimal>result:
                    result = item-minimal
        return result
