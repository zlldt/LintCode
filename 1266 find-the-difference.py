class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        # Write your code here
        lists=list(s)
        listt=list(t)
        for i in lists:
            listt.remove(i)
        return listt[0]
