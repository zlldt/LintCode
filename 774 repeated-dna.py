class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences 
    """
    def findRepeatedDna(self, s):
        # write your code here
        result = []
        temp = {}
        length =len(s)
        for x in range(length-9):
            substr = s[x:x+10]
            if substr not in temp:
                temp[substr] = 1
            else:
                temp[substr] += 1
        for key,value in temp.items():
            if value > 1:
                result.append(key)
        print(result)
        return result


test=Solution()
test.findRepeatedDna('AAAAAAAAAAA')
