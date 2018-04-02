import queue
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        # write your code here
        q = queue.PriorityQueue()
        for i in nums:
            q.put((-i,i))
        result = []
        for i in range(k):
            result.append(q.get()[1])
        return result
