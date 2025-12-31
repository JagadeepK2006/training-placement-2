class Solution(object):
    def maxScore(self, s):
        a=0
        for i in range(1,len(s)):
            x=s[:i]
            y=s[i:]
            a=max((x.count("0")+y.count("1")),a)
        return a
