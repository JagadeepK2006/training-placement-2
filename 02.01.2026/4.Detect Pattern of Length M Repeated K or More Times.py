class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        l=len(arr)
        for i in range(l-m*k+1):
            p=arr[i:i+m]
            if arr[i:i+k*m]==p*k:
                return True
        return False
        
