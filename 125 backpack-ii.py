class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        length = len(A)
        dp = [0 for x in range(m+1)]
        value = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        maxvalue = 0
        for item in range(length):
            for i in range(m,-1,-1):
                if i-A[item]>=0 and dp[i-A[item]]>0:
                    value[i] = max(value[i], value[i-A[item]] + V[item])
                    maxvalue = max(maxvalue, value[i])
                    ans = max(ans, i)
                    dp[i]=1
            # print(maxvalue,value)
        return maxvalue


test=Solution()
test.backPackII(100,[77,22,29,50,99],[92,22,87,46,90])
