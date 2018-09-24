class Solution:
    """
    @param arr: the arr
    @return: the sum
    """
    def takeTheElementAndQueryTheSum(self, arr):
        # Write your code here
        sum1 = 0
        length = len(arr)
        # for x in range(length-1):
        #     for y in range(x+1,length):
        #         sum += ((arr[x]%1000000007)*(arr[y]%1000000007))%1000000007
        #         sum = sum%1000000007
        # return sum
        
        arrsum = sum(arr)
        sub = 0
        for x in range(length):
            # sum1 += (((arrsum-arr[x])%1000000007)*(arr[x]%1000000007))
            sub += arr[x]*arr[x]
        # sum1=(sum1//2)%1000000007
        sum1 = ((arrsum**2-sub)//2)%1000000007
        return sum1
