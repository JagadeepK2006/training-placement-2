class Solution:
    def totalHammingDistance(self, a):
        r=0; n=len(a)
        for i in range(32):
            c=sum((x>>i)&1 for x in a)
            r+=c*(n-c)
        return r
