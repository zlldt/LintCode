class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        result = []
        if n==0 or n==1:
            return True
        while n>1:
            result.append(n%2)
            n = n//2
        result.append(1)
        length = len(result)
        count = 0
        while count<(length-count-1):
            if not result[count]==result[length-count-1]:
                return False
            count +=1
        return True
