class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        n=-1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    n=max(n,j-i-1)
        return n
        
