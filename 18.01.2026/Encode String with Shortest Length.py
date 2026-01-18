class Solution:
    def encode(self, s):
        n=len(s)
        dp=[[""]*n for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                j=i+l
                dp[i][j]=s[i:j+1]
                if l<4: continue
                for k in range(i,j):
                    if len(dp[i][k]+dp[k+1][j])<len(dp[i][j]):
                        dp[i][j]=dp[i][k]+dp[k+1][j]
                t=(s[i:j+1]+s[i:j+1]).find(s[i:j+1],1)
                if t<l+1:
                    e=str((l+1)//t)+"["+dp[i][i+t-1]+"]"
                    if len(e)<len(dp[i][j]): dp[i][j]=e
        return dp[0][n-1]
