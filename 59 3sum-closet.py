#Author: zlldt
#Date: 2018/2/20
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        length = len(numbers)
        numbers.sort()
        maxvalue = abs(target - (numbers[0]+numbers[1]+numbers[2]))
        value = numbers[0]+numbers[1]+numbers[2]
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if numbers[i] + numbers[j] + numbers[k] - target >= 0 and \
                            (numbers[i] + numbers[j] + numbers[k] - target <= maxvalue):
                        maxvalue = numbers[i] + numbers[j] + numbers[k] - target
                        value = numbers[i] + numbers[j] + numbers[k]
                        if maxvalue == 0:
                            return value
                        break
                    elif target - (numbers[i] + numbers[j] + numbers[k]) >= 0 and \
                            target -(numbers[i] + numbers[j] + numbers[k]) <= maxvalue:
                        maxvalue = target - (numbers[i] + numbers[j] + numbers[k])
                        value = numbers[i] + numbers[j] + numbers[k]
        return value
