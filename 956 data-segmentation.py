class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, str):
        # Write your code here
        result = []
        temp = ''
        for i in str:
            #空格
            if i == ' ':
                if not temp == '':
                    result.append(temp)
                    temp = ''
            #字母
            elif (i >= 'a') and (i <= 'z'):
                temp = temp + i
                print("debug2:temp=",temp)
            #符号
            else:
                if not temp == '':
                    result.append(temp)
                    temp = ''
                result.append(i)
        if not temp == '':
            result.append(temp)
        return result
