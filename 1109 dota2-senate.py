class Solution:
    """
    @param senate: a string
    @return: return a string
    """
    def predictPartyVictory(self, senate):
        # write your code here
        rcount=0
        dcount=0
        
        for i in senate:
            if i is 'R':
                rcount+=1
                if rcount>0:
                    dcount-=1
            else:
                dcount+=1
                if dcount>0:
                    rcount-=1
        if rcount>dcount:
            return 'Radiant'
        elif rcount<dcount:
            return 'Dire'
        if senate[0] is 'R':
            return 'Radiant'
        else:
            return 'Dire'
