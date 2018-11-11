class Solution:
    """
    @param n: a positive integer n
    @return: the maximum product you can get
    """
    def integerBreak(self, n):
        # Write your code here
        product=[1,1]
        for x in range(3,n+1):
            product.append(1)
            for y in range(1,x):
                if y*product[x-y-1]>product[x-1]:
                    product[x-1]=y*product[x-y-1]
                elif y*(x-y)>product[x-1]:
                    product[x-1]=y*(x-y)
        return product[-1]
