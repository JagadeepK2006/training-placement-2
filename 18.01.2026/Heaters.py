class Solution:
    def findRadius(self, h, r):
        import bisect
        r.sort()
        ans=0
        for x in h:
            i=bisect.bisect_left(r,x)
            d=min(abs(x-r[i]) if i<len(r) else 10**18,
                  abs(x-r[i-1]) if i else 10**18)
            ans=max(ans,d)
        return ans
