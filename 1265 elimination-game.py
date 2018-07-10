class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def lastRemaining(self, n):
        # write your code here
        # result = [x for x in range(1,n+1)]
        # while len(result)>1:
        #     temp = []
        #     length = len(result)
        #     for x in range(1,length,2):
        #         temp.append(result[x])
        #     temp.reverse()
        #     result = temp
        # return result[0]
        low, high = 1, n
        gap = 1
        # direction 0 left to right
        # direction 1 right to left
        direction = 0
        while high > low:
            n = (high - low) // gap
            if direction == 0:
                low += gap
                if n % 2 == 0:
                    high -= gap
                direction = 1
            else:
                high -= gap
                if n % 2 == 0:
                    low += gap
                direction = 0
            gap *= 2
        return low
