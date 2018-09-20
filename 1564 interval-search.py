class Solution:
    """
    @param intervalList: 
    @param number: 
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        # Write your code here
        for start,end in intervalList:
            if number>=start and number<=end:
                return 'True'
        return 'False'
