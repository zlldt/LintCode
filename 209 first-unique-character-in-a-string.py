class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        strset =set()
        notuniqueset =set()
        uniqueset =set()
        for char in str:
            if char not in strset:
                strset.add(char)
            else:
                notuniqueset.add(char)
        uniqueset = strset - notuniqueset
        for char in str:
            if char in uniqueset:
                return char
