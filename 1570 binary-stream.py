class Solution:
    """
    @param s: the binary stream
    @return: the outputs
    """
    def getOutput(self, s):
        # Write your code here
        value = 0
        length = len(s)
        result = []
        for i in range(length):
            if s[i]=='0':
                value = (value*2)%3
            else:
                value = (value*2+1)%3
            if value==0:
                result.append(i+1)
        return result
