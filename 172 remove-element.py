class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        if A is None:
            # print(0)
            return 0
        length = len(A)
        count = 0

        while A.count(elem) > 0:
            A.remove(elem)
            count += 1
        # print(length-count)
        return length - count
