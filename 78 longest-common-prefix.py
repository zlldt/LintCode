class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs)==0:
            return ''
        result = strs[0]
        length = len(strs)
        for i in range(1,length):
            print(result)
            result = self.getCommon(result,strs[i])
        return result

    def getCommon(self, strA, strB):
        lenA = len(strA)
        lenB = len(strB)
        result = ''
        length = min(lenA, lenB)
        for i in range(length):
            if strA[i]==strB[i]:
                result = result + strA[i]
            else:
                return result
        return result
