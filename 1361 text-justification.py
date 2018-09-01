class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """

    def getSpaceCount(self, totalspacecount, seq, count):
        if totalspacecount % (count - 1) == 0:
            return totalspacecount // (count - 1)
        else:
            base = totalspacecount // (count - 1)
            if seq < totalspacecount % (count -1):
                return base+1
            else:
                return base


    def fullJustify(self, words, maxWidth):
        # write your code here
        result = []
        result1 = []
        tempstring = []
        spacecount = []
        stringlength = 0
        wordlength = 0
        for word in words:
            if stringlength + len(word) <= maxWidth:
                tempstring.append(word)
                stringlength += len(word) + 1
                wordlength += len(word)
            else:
                result.append(tempstring)
                spacecount.append(maxWidth - wordlength)
                tempstring = []
                stringlength = 0
                wordlength = 0
                tempstring.append(word)
                stringlength += len(word) + 1
                wordlength += len(word)
        spacecount.append(maxWidth - wordlength)
        result.append(tempstring)
        resultcount = len(result)
        for y in range(resultcount - 1):
            tempstring = []
            if len(result[y]) > 1:
                tempstring = result[y][0]
                for seq in range(len(result[y]) - 1):
                    tempstring += ' ' * (self.getSpaceCount(spacecount[y], seq, len(result[y]))) + result[y][seq + 1]
            else:
                tempstring = result[y][0]+' '*(maxWidth-len(result[y][0]))
            result1.append(tempstring)
        tempstring = result[-1][0]
        for seq in range(1, len(result[-1])):
            tempstring += ' '+result[-1][seq]
        if len(tempstring)<maxWidth:
            tempstring += ' '*(maxWidth-len(tempstring))
        result1.append(tempstring)
        return result1
