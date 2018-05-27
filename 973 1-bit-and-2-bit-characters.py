class Solution:
    """
    @param bits: a array represented by several bits. 
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        # Write your code here
        length = len(bits)
        if length == 1:
            return True
        if bits[0] == 0:
            flag = 2
        else:
            flag = 1
        #stats: 2 --one-bit 0 
        #stats: 1 --first  bit of 10 or 11
        #stats: 0 --second bit of 10 or 11
        for x in range(1, length):
            if flag == 1:
                flag = 0
            elif bits[x]==1:# and flag == 0:
                flag = 1
            # elif bits[x]==1 and flag == 2:
            #     flag = 1
            
            # elif bits[x]==0:# and flag == 0:
            #     flag = 2
            # elif bits[x]==0 and flag == 2:
            #     flag = 2
            else:
                flag = 2
        if flag == 2:
            return True
        return False
