class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        b=0
        a=2*n+start
        for i in range (start,a,2):
            b=b^i
        return b
        
        
