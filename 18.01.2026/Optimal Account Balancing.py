class Solution:
    def minTransfers(self, t):
        from collections import defaultdict
        d=defaultdict(int)
        for a,b,c in t:
            d[a]-=c; d[b]+=c
        a=[x for x in d.values() if x]
        def dfs(i):
            while i<len(a) and a[i]==0: i+=1
            if i==len(a): return 0
            r=10**9
            for j in range(i+1,len(a)):
                if a[i]*a[j]<0:
                    a[j]+=a[i]
                    r=min(r,1+dfs(i+1))
                    a[j]-=a[i]
            return r
        return dfs(0)
