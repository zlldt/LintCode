class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitchWords(self, str):
        # Write your code here
        result = []
        length = len(str)
        count = 1
        for i in range(1, length):
            if str[i]==str[i-1]:
                count += 1
            else:
                if count>2:
                    result.append([i-count ,i-1])
                count = 1
        if count>2:
            result.append([i-count+1,i])
        return result
