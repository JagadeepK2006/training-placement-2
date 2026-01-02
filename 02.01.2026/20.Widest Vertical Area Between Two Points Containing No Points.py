class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = []
        for i in points:
            ans.append(i[0])
        sort_ans = sorted(ans)
        result = []
        for j in range(0, len(sort_ans)-1):
            var=sort_ans[j+1]-sort_ans[j]
            result.append(var)

        return max(result)
