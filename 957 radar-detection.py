"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param coordinates: The radars' coordinate
    @param radius: Detection radius of radars
    @return: The car was detected or not
    """
    def radarDetection(self, coordinates, radius):
        # Write your code here
        for point in coordinates:
            if point.y+radius[-1]>=1 and point.y-radius[-1]<=0:
                return 'YES'
        return 'NO'
