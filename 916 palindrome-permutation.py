class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        length = len(s)
        dict ={}
        for i in range(length):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
        if len(dict)==1:
            return True
        count = 0
        for k,v in dict.items():
            if v % 2 == 1:
                count += 1
            if count>1:
                return False
        return True
