class Solution:
    """
    @param nums: an array of integer
    @return: the first missing prime number
    """
    def firstMissingPrime(self, nums):
        # write your code here
        if nums==[]:
            return 2
        maxval = max(nums)
        primelist = self.PrimeList(maxval)
        for i in range(len(primelist)):
            if nums.count(primelist[i]) == 0:
                return primelist[i]
        maxprime = primelist[len(primelist)-1]

        primevalue = maxval+1
        count = 1
        while count > 0:
            tempcount = 0
            for i in range(len(primelist)):
                if (primevalue % primelist[i])>0:
                    tempcount += 1
            if tempcount == len(primelist):
                return primevalue
            primevalue += 1
            count = tempcount


    def PrimeList(self, n):
        # write your code here
        value = [1 for i in range(n+1)]
        value[0] = 0
        value[1] = 0
        temp = 0
        result = []
        for i in range(2, (n+1)//2):
            temp = i * 2
            if temp > n:
                break
            while temp < n:
                value[temp] = 0
                temp += i
        for i in range(n):
            if value[i]==1:
                result.append(i)
        return result
