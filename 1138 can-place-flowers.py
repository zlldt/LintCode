class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        add = 0
        count = 0
        for i in flowerbed:
            if i==0:
                count+=1
            if i==1:
                if count>2:
                    add += (count-1)//2
                count = 0
        if add < n:
            return False
        return True
