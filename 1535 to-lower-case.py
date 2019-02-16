class Solution:
    """
    @param str: the input string
    @return: The lower case string
    """
    def toLowerCase(self, str):
        # Write your code here
        target=''
        sub=ord('A')-ord('a')
        for char in str:
            if ord(char)>=ord('A') and ord(char)<=ord('Z'):
                target+=chr(ord(char)-sub)
            else:
                target+=char
        return target
