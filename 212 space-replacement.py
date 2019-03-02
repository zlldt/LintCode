class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if string is None:
            return 0
        count=string.count(' ')
        newlength = length+count*2
        for x in range(length-1,-1,-1):
            if string[x] is not ' ':
                string[x+count*2]=string[x]
            else:
                string[x+count*2]='0'
                string[x+count*2-1]='2'
                string[x+count*2-2]='%'
                count-=1
        return newlength
