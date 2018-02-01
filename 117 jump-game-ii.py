class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        length = len(A)
        B = [0 for col in range(len(A))]
        for i in range(length):
            if A[length-i-1] >= i:
                B[length-i-1] = 1
            else:
                temp = B[length-i-1+A[length-i-1]]+1
                for j in range(A[length-i-1]):
                    if temp > B[length-i-1-j+A[length-i-1]]+1:
                        temp = B[length-i-1-j+A[length-i-1]]+1
                B[length-i-1] = temp
        print(B)
        return B[0]

test=Solution()

print(test.jump([2,3,1,1,4]))
