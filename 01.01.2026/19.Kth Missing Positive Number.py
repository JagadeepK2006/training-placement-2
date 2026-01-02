class Solution(object):
    def findKthPositive(self, arr, k):
        w = k
        for j in arr:
            if j <= w:
                w += 1
        return w
