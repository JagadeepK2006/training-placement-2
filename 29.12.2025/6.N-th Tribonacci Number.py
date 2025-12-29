class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tri=[0,1,1]
        k=n
        while k>0:
            tri.append(tri[-3]+tri[-2]+tri[-1])
            k-=1
        return tri[n]
        
