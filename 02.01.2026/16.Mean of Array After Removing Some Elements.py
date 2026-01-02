class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        n=len(arr)
        k=n//20
        arr.sort()
        trimmed=arr[k:n-k]
        return sum(trimmed)/float(len(trimmed))
