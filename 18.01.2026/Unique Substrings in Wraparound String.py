class Solution:
    def findSubstringInWraproundString(self, p):
        dp=[0]*26
        k=0
        for i,c in enumerate(p):
            if i and (ord(c)-ord(p[i-1]))%26==1:
                k+=1
            else:
                k=1
            dp[ord(c)-97]=max(dp[ord(c)-97],k)
        return sum(dp)
