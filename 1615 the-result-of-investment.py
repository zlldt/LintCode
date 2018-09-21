class Solution:
    """
    @param funds: The investment each time
    @param a: The initial funds of A
    @param b: The initial funds of B
    @param c: The initial funds of C
    @return: The final funds
    """
    def getAns(self, funds, a, b, c):
        # Write your code here
        for fund in funds:
            if a<=b and a<=c:
                a+=fund
            elif b<a and b<=c:
                b+=fund
            elif c<a and c<b:
                c+=fund
        return [a,b,c]
