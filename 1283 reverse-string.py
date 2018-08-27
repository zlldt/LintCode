class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        # 1st
        # if s is None:
        #     return s
        # newstring = ''
        # for char in s:
        #     newstring = char+newstring
        # return newstring
        
        # 2nd
        # slist = list(s)
        # slist.reverse()
        # newstring = ''.join(slist)
        # return newstring
        
        # 3rd
        return ''.join(reversed(s))        
