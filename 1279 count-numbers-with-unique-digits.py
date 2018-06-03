class Solution:
    """
    @param n: a non-negative integer
    @return: number of numbers with unique digits
    """
    def countNumbersWithUniqueDigits(self, n):
        # Write your code here 
        base = 10
        result = base
        base2 = 9
        i=1
        while i<n:
            base2 *= (10-i)
            result += base2            
            i+=1
        return result
