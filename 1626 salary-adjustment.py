class Solution:
    """
    @param a: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, a, target):
        # Write your code here.
        a=sorted(a)
        low = a[0]
        high = a[-1]
        index = (low + high) // 2
        # print(target-sum(a))
        result = sum(a)
        for x in range(len(a)):
            if a[x] < index:
                result += index-a[x]
            else:
                break
        # print(result)
        while not result == target:
            if result > target:
                # print('result>target', )
                high = index
            else:
                # print('result<target', )
                low = index
            index = (low + high) // 2
            result = sum(a)
            for x in range(len(a)):
                if a[x] < index:
                    result += index-a[x]
                else:
                    break
            # print(result)
        # print(index)
        return index
