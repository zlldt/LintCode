class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """
    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        magazinedict = {}
        for letter in magazine:
            if letter in magazinedict:
                magazinedict[letter] +=1
            else:
                magazinedict[letter] =1
        for letter in ransomNote:
            if letter in magazinedict:
                if magazinedict[letter]==0:
                    return False
                else:
                    magazinedict[letter] -= 1
            else:
                return False
        return True
