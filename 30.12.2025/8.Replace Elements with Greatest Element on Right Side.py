class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        n = len(arr)
        count = max_count = 0
        
        for i in range(n-1, -1, -1):
            count = arr[i]
            if i == n-1:
                arr[i] = -1
                
            else:
                arr[i] = max_count
            
            if max_count < count:
                max_count = count
        
        return arr
            
        
