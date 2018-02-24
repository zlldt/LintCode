#Author: zlldt
#Date: 2018/2/18
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        list = []
        zipnumbers = []
        length = len(numbers)
        numbers.sort()
        for i in range(length):
            if numbers.count(numbers[i])>4:
                if zipnumbers.count(numbers[i])==0:
                    zipnumbers.append(numbers[i])
                    zipnumbers.append(numbers[i])
                    zipnumbers.append(numbers[i])
                    zipnumbers.append(numbers[i])
            else:
                zipnumbers.append(numbers[i])
                
        ziplength = len(zipnumbers)
        for i in range(ziplength-3):
            if (zipnumbers[i]+zipnumbers[ziplength-3]+zipnumbers[ziplength-2]+zipnumbers[ziplength-1]) < target:
                continue
            else:
                for j in range(i+1, ziplength-2):
                    if (zipnumbers[i]+zipnumbers[j]+zipnumbers[ziplength-2]+zipnumbers[ziplength-1]) < target:
                        continue
                    else:
                        for k in range(j+1, ziplength-1):
                            # if (zipnumbers[i]+zipnumbers[j]+zipnumbers[k]+zipnumbers[ziplength-1]) < target:
                            #     continue
                            # else:
                            for l in range(k+1, ziplength):
                                if (zipnumbers[i]+zipnumbers[j]+zipnumbers[k]+zipnumbers[l])==target:
                                    if list.count([zipnumbers[i],zipnumbers[j],zipnumbers[k],zipnumbers[l]])==0:
                                        list.append([zipnumbers[i],zipnumbers[j],zipnumbers[k],zipnumbers[l]])
                                    break
        return list
