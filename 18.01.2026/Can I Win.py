class Solution:
    def canIWin(self, m, t):
        if t<=0: return True
        if m*(m+1)//2<t: return False
        from functools import lru_cache
        @lru_cache(None)
        def dfs(u,s):
            for i in range(1,m+1):
                if not (u>>i)&1:
                    if i>=s or not dfs(u|(1<<i),s-i):
                        return True
            return False
        return dfs(0,t)
