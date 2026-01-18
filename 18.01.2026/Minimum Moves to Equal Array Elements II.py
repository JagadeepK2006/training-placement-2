class Solution:
    def minMoves2(self, a):
        a.sort()
        m=a[len(a)//2]
        return sum(abs(x-m) for x in a)
