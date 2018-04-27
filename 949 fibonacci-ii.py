class Solution:
    """
    @param n: an integer
    @return: return a string
    """
    def lastFourDigitsOfFn(self, n):
        # write your code here
        if n==0:
            return '0'
        if n==1:
            return '1'
        if n>=15000:
            n = n%15000
        numbers = [0 for x in range(n+1)]
        numbers[0]=0
        numbers[1]=1
        for x in range(2,n+1):
            numbers[x]=(numbers[x-1]%10000+numbers[x-2]%10000)%10000
        return str(numbers[n])
