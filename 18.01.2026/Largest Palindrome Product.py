class Solution:
    def largestPalindrome(self, n):
        if n==1: return 9
        u=10**n-1
        l=10**(n-1)
        for x in range(u,l,-1):
            p=int(str(x)+str(x)[::-1])
            for y in range(u,int(p**0.5),-1):
                if p%y==0:
                    return p%1337
