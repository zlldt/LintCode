class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        # Write your code here
        length = len(s)

        result = [1 for x in range(length)]
        dict ={}
        for i in range(length):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
            if len(dict)==1:
                result[i] = 1
            count = 0
            for k,v in dict.items():
                if v % 2 == 1:
                    count += 1
            if count>1:
                result[i] = 0
        return result
