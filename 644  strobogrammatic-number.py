class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        dict = {"6":"9","9":"6","8":"8","0":"0","1":"1"}
        newstring = []
        for x in range(len(num)-1,-1,-1):
            if num[x] not in dict:
                return False
            newstring.append(dict[num[x]])
        if num == ''.join(newstring):
            return True
        return False
