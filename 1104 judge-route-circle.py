class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        position=[0,0]
        for move in moves:
            if move=='R':
                position[0]+=1
            elif move=='L':
                position[0]-=1
            elif move=='U':
                position[1]+=1
            elif move=='D':
                position[1]-=1
        if position==[0,0]:
            return True
        return False
