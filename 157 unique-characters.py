class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        dict ={}
        for i in str:
            if i in dict:
                return False
            else:
                dict[i]=1
        return True
