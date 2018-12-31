class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """
    def uniqueMorseRepresentations(self, words):
        # Write your code here
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations=[]
        for word in words:
            transformation = ""
            for char in word:
                transformation+=code[ord(char)-ord('a')]
            if transformation not in transformations:
                transformations.append(transformation)
        return len(transformations)
