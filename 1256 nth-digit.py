class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    def findNthDigit(self, n):
        # write your code here
        # count =[9,90,900,9000]
        basecount = 9
        basedigit = 1
        baselength = 1
        digitcount = basecount*baselength
        #找到对应的数位长度
        temp = n
        while temp>digitcount:
            temp = temp-digitcount
            basecount*=10
            basedigit*=10
            baselength+=1
            digitcount = basecount*baselength
        #找到对应的数字是多少
        if baselength==1:
            return n
        if temp%baselength==0:
            targetnumber= basedigit+temp//baselength -1
            return targetnumber%10
        else:
            targetnumber= basedigit+temp//baselength
            nthdigit = temp%baselength
            lowernthdigit = baselength - nthdigit
        for x in range(lowernthdigit):
            targetnumber = targetnumber //10
        return targetnumber%10
        
        
