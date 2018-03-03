class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        result = []
        length = len(digits)
        promotion = 1
        for i in range(length-1, -1, -1):
            if digits[i] <9 and promotion == 1:
                promotion = 0
                result.append(digits[i]+1)
            elif promotion == 0:
                result.append(digits[i])
            elif digits[i] == 9 and promotion == 1:
                promotion = 1
                result.append(0)
        if promotion == 1:
            result.append(1)
        result.reverse()
        return result
