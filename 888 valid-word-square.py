class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        cols = map(''.join, zip(*words))
        lines = list(cols)
        length = len(lines)
        for i in range(length):
            if not words[i] == lines[i]:
                return False
        return True
