class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def originalDigits(self, s):
        # write  your code here
        count = [0 for x in range(10)]
        if 'z' in s:
            count[0]=s.count('z')
        if 'w' in s:
            count[2]=s.count('w')
        if 'u' in s:
            count[4]=s.count('u')
        count[1]=s.count('o')-count[0]-count[2]-count[4]
        count[3]=s.count('r')-count[0]-count[4]
        count[5]=s.count('f')-count[4]        
        if 'x' in s:
            count[6]=s.count('x')
        count[7]=s.count('s')-count[6]
        count[8]=s.count('t')-count[2]-count[3]
        count[9]=s.count('i')-count[5]-count[6]-count[8]
        result = ""
        for x in range(10):
            result+=str(x)*count[x]
        return result
