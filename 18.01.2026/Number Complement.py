class Solution:
    def findComplement(self, n):
        b=bin(n)[2:]
        return int(''.join('1' if c=='0' else '0' for c in b),2)
