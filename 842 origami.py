class Solution:
    """
    @param n: The folding times
    @return: the 01 string
    """
    def getString(self, n):
        # Write your code here
        # result = '0'
        # left = '0'
        # right = '1'
        # if n == 1:
        #     return '0'
        # if n >= 2:
        #     result = left + result + right
        #
        # for i in range(3, n+1):
        #     temp = []
        #     add = '01'*(2**(i-1))
        #     for x in range(len(result)):
        #         temp.append(add[x])
        #         temp.append(result[x])
        #     temp += add[2**(i-1)-1]
        #     result = ''.join(temp)
        result = '0'
        right = '1'
        for i in range(1, n):
            result, right = result+'0'+right, result+'1'+right
        # print(result)
        return result

test=Solution()
test.getString(12)
