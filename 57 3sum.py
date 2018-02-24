#Author: zlldt
#Date: 2018/2/21
class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        list = []
        length = len(numbers)
        numbers.sort()
        zipnumbers = []
        for i in range(length):
            if numbers.count(numbers[i]) > 3:
                if zipnumbers.count(numbers[i]) == 0:
                    zipnumbers.append(numbers[i])
                    zipnumbers.append(numbers[i])
                    zipnumbers.append(numbers[i])
            else:
                zipnumbers.append(numbers[i])
        ziplength = len(zipnumbers)

        for i in range(ziplength - 2):
            if (zipnumbers[i] + zipnumbers[ziplength - 2] + zipnumbers[ziplength - 1]) < 0:
                continue
            else:
                for j in range(i + 1, ziplength - 1):
                    if (zipnumbers[i] + zipnumbers[j] + zipnumbers[ziplength - 1]) < 0:
                        continue
                    else:
                        for k in range(j + 1, ziplength):
                            if zipnumbers[i] + zipnumbers[j] + zipnumbers[k] == 0:
                                if list.count([zipnumbers[i], zipnumbers[j], zipnumbers[k]]) == 0:
                                    list.append([zipnumbers[i], zipnumbers[j], zipnumbers[k]])
                                break
        return list
