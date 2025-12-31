class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count=0
        for i in range(len(points)-1):
            for j in range(len(points[i])-1):
                count+=max(abs(points[i][j]-points[i+1][j]),abs(points[i][j+1]-points[i+1][j+1]))
        return count
