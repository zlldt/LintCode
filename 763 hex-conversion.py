class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """
    def hexConversion(self, n, k):
        # write your code here
        result = []
        while n>=k:
            value = n%k
            if value==0:
                result.append('0')
            else:
                if value<10:
                    result.append(str(value))
                else:
                    result.append(chr(ord('A')+value-10))
            n = n//k
        if n<10:
            result.append(str(n))
        else:
            result.append(chr(ord('A')+n-10))
        result.reverse()
        return ''.join(result)
