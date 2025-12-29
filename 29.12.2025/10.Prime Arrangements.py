class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=0
        for i in range(1,n+1):
            p += self.prime(i)
        np = n-p
        return (self.fact(p) * self.fact(np)) % (10**9 + 7)

    
    def fact(self,n):
        if n<=1:
            return 1
        return n*self.fact(n-1)
         
    def prime(self,n):
        if n<2:
            return 0
        i=2
        while i*i <= n:
            if n%i == 0:
                return 0
            i+=1
        return 1 
