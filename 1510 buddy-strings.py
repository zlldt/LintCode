class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        # Write your code here
        if not sorted(A)==sorted(B):
            return False
        if A==B and len(set(A))>1:
            if len(A)>2:
                return True
            else:
                return False
        if not len(A)==len(B):
            return False
        length = len(A)
        count=0
        for x in range(length):
            if not A[x]==B[x]:
                count+=1
        if count>2 or count==1:
            return False
        # if not set(A)==set(B):
        #     return False
        return True
