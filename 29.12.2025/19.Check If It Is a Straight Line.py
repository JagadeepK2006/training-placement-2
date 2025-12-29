
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates)==2:
            return True
        p1=coordinates[0]
        p2=coordinates[1]
        numerator=p2[1]-p1[1]
        denominator=p2[0]-p1[0]

        for point in coordinates[2:]:
            n=point[1]-p2[1]
            d=point[0]-p2[0]
            if numerator*d !=n*denominator:
                return False
        return True

        
