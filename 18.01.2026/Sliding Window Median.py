class Solution:
    def medianSlidingWindow(self, a, k):
        import bisect
        w=[]; r=[]
        for i,x in enumerate(a):
            bisect.insort(w,x)
            if i>=k:
                w.pop(bisect.bisect_left(w,a[i-k]))
            if i>=k-1:
                r.append(w[k//2] if k%2 else (w[k//2-1]+w[k//2])/2)
        return r
