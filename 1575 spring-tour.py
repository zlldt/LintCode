class Solution:
    """
    @param a: The array a
    @return: Return the minimum number of car
    """
    def getAnswer(self, a):
        # Write your code here
        a1 = a.count(1)
        a2 = a.count(2)
        a3 = a.count(3)
        a4 = a.count(4)
        if a3>=a1:
            return a4+a3+a2//2+(1 if a2%2==1 else 0)
        else:
            return a4+a3+a2//2+(1 if a2%2==1 else 0) + (a1-a3-(2 if a2%2==1 else 0))//4+(1 if (a1-a3-(2 if a2%2==1 else 0))%4>0 else 0)
