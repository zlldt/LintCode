class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        # write your code here
        count = 0
        for char in s:
            count = count*26+ord(char)-ord("A")+1
        return count
