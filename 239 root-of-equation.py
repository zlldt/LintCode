import math
class Solution:
    """
    @param: a: parameter of the equation
    @param: b: parameter of the equation
    @param: c: parameter of the equation
    @return: a double array, contains at most two root
    """
    def rootOfEquation(self, a, b, c):
        # write your code here
        result=[]
        d = b*b - 4*a*c
        if d>0:
            result.append(-b/2/a-math.sqrt(d)/2/a)
            result.append(-b/2/a+math.sqrt(d)/2/a)
            result=sorted(result)
        elif d==0:
            result.append(-b/2/a)
        return result
