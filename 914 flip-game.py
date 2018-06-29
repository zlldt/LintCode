class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """

    def generatePossibleNextMoves(self, s):
        result = []
        length = len(s)
        for i in range(length - 1):
            if s[i] == '+' and s[i + 1] == '+':
                tempstr = s[0:i] + '--' + s[i + 2:]
                result.append(tempstr)
        return result
