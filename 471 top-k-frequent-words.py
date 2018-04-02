import queue


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        # write your code here
        q = queue.PriorityQueue()
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        for item in dict:
            q.put((-dict[item], item))
        result = []
        for i in range(k):
            result.append(q.get()[1])
        return result
