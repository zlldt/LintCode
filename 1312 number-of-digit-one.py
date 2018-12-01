class Solution:
    """
    @param n: an integer 
    @return: the total number of digit 1
    """
    def countDigitOne(self, n):
        # write your code here
        if n<1:
            return 0
        if n<10:
            return 1
        elif n==10:
            return 2
        # elif n==11:
        #     return 4
        # elif n<20:
        #     return 2+n-10+1 #20以下 n-7
        # elif n==20:
        #     return 12
        # elif n<30:
        #     return 13
        # elif n<40:
        #     return 14
        # elif n<100:
        #     # return 11+n//10
        #     return self.countDigitOne(10)+9+self.countDigitOne(n%10)+self.countDigitOne(9)*(n//10-1)
        # elif n==100:
        #     return 21
        # elif n<=200:
            #1-100,101-199,200,201----2xx
            #count(100)+n-100+count(xx)
        #     return self.countDigitOne(100)+n-100+self.countDigitOne(n-100)
        # elif n<1000:
        #     return self.countDigitOne(100)+99+self.countDigitOne(n%100)+self.countDigitOne(99)*(n//100-1)
        # elif n==1000:
        #     return self.countDigitOne(999)+1
        # elif n<2000:
        #     return self.countDigitOne(1000)+n%1000+self.countDigitOne(n%1000)
        # elif n<10000:
        #     return self.countDigitOne(1000)+999+self.countDigitOne(n%1000)+self.countDigitOne(999)*(n//1000-1)
        else:
            # base=10
            # while base<n:
            #     base*=10
            # base = base//10
            # if n>base*2:
            #     return base+n%base+self.countDigitOne(n%base)
            base=10
            while base<=n:
                base*=10
            base = base//10
            if base==n:
                return self.countDigitOne(base-1)+1
            if n<base*2:
                return self.countDigitOne(base)+n%base+self.countDigitOne(n%base)
            return self.countDigitOne(base)+base-1+self.countDigitOne(n%base)+self.countDigitOne(base-1)*(n//base-1)
