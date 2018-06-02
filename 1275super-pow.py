class Solution:
    """
    @param a: the given number a
    @param b: the given array
    @return: the result
    """

    def superPow(self, a, b):
        result = 1
        if a > 1337:
            a = a % 1337
        if a == 1:
            return 1
        b.reverse()
        base = a
        for i in b:
            value = 1
            if i > 0:
                for temp in range(i):
                    value = value * base % 1337
            nextbase = 1
            for temp in range(10):
                nextbase = nextbase * base % 1337
            result = result * value % 1337
            base = nextbase
        return result


test = Solution()
print(test.superPow(2147483647, [2, 0, 0]))
