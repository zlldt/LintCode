class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        # Write your code here
        length = len(ages)
        count = 0
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                elif ages[j]<=(ages[i]//2+7):
                    continue
                elif ages[j] > ages[i]:
                    continue
                elif ages[j] < 100 and ages[i] > 100:
                    continue
                else:
                    count += 1
        return count
