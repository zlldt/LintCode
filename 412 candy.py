class Solution:
    """
    @param ratings: Children's ratings
    @return: the minimum candies you must give
    """
    def candy(self, ratings):
        # write your code here
        length = len(ratings)
        result = [1 for x in range(length)]
        # flag = False
        count = 0
        while count<(length-1):
            count = 0
            for x in range(length - 1):
                # if x>0 or x<length-1:
                if ratings[x] > ratings[x + 1]:
                    if result[x] <= result[x + 1]:
                        result[x] = result[x + 1] + 1
                    else:
                        count+=1
                if ratings[x] < ratings[x + 1]:
                    if result[x] >= result[x + 1]:
                        result[x + 1] = result[x] + 1
                    else:
                        count+=1
                if ratings[x] == ratings[x + 1]:
                    # if result[x] > result[x + 1]:
                    #     result[x + 1] = result[x]
                    # elif result[x] < result[x + 1]:
                    #     result[x] = result[x + 1]
                    # else:
                    count+=1
        # print(result)
        # print(sum(result))
        return sum(result)
