class Solution:
    """
    @param timeSeries: the Teemo's attacking ascending time series towards Ashe
    @param duration: the poisoning time duration per Teemo's attacking
    @return: the total time that Ashe is in poisoned condition
    """
    def findPoisonedDuration(self, timeSeries, duration):
        # Write your code here
        totaltime = 0
        endtime = 0
        for x in timeSeries:
            if x>endtime:
                endtime = x+duration
                totaltime += duration
            elif (x<=endtime) and (x+duration>endtime):
                totaltime -=endtime-x-duration
                endtime = x+duration
            else:
                continue
        return totaltime
