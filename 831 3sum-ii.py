class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    def threeSum2(self, n):
        # Write your code here
        result = []
        x, y = 0, 0
        max = int(math.sqrt(n))
        for x in range(max + 1):
            for y in range(x, max + 1):
                left = n - x * x - y * y
                if left < x * x or left < y * y:
                    break
                z = int(math.sqrt(left))
                if z * z == left:
                    if [x, y, z] not in result:
                        result.append([x, y, z])
        return len(result)
