class Solution:
    def findMaxForm(self, s, m, n):
        dp=[[0]*(n+1) for _ in range(m+1)]
        for x in s:
            z=x.count('0'); o=x.count('1')
            for i in range(m,z-1,-1):
                for j in range(n,o-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-z][j-o]+1)
        return dp[m][n]
