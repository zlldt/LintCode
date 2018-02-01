#Author: zlldt
#Date: 2018/2/1
class Solution:
    """
    @param: n: a positive integer
    @param: primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        primes.sort()
        uglynumber = []
        temp = 1
        if n == 1:
            return 1
        uglynumber.append(1)
        uglynumber.append(primes[0])
        for i in range(2,n):
            for uglycount in range(i):
                for primecount in  range(len(primes)):
                    if uglynumber[uglycount]*primes[primecount]>uglynumber[i-1]:
                        if temp <= uglynumber[i - 1]:
                            temp = uglynumber[uglycount] * primes[primecount]
                        elif temp > uglynumber[uglycount] * primes[primecount]:
                            #print("debug2:>","i=",i,"ugly_count=",ugly_count,"prime_count=",prime_count,"temp=",temp,"multiply=",uglynumber[ugly_count]*primes[prime_count])
                            temp = uglynumber[uglycount] * primes[primecount]
            uglynumber.append(temp)
        print(uglynumber)
        return uglynumber[n-1]


test = Solution()
print(test.nthSuperUglyNumber(20, [2, 7, 13, 19]))
