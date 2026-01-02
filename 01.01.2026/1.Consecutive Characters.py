class Solution(object):
    def maxPower(self, s):
        maxcount=1
        currentcount=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                currentcount+=1
                maxcount=max(maxcount,currentcount)
            else:
                currentcount=1
        return maxcount
