class Solution:
    def makesquare(self, a):
        s=sum(a)
        if s%4: return False
        t=s//4
        a.sort(reverse=True)
        b=[0]*4
        def dfs(i):
            if i==len(a): return True
            for j in range(4):
                if b[j]+a[i]<=t:
                    b[j]+=a[i]
                    if dfs(i+1): return True
                    b[j]-=a[i]
            return False
        return dfs(0)
